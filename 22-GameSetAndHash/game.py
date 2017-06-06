import socket
import requests
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendMsg(msg):
	sock.sendall(msg)


def readMsg():
	return sock.recv(4096)


def awaitMsg(expected):
	msg = readMsg()
	if msg != expected:
		raise Exception("Unexpected message, expected:\n%s\ngot:\n%s" % (expected, msg))


def lookupHash(h):
	r = requests.get('http://hashtoolkit.com/reverse-hash?hash=' + h)
	match = re.search(r'<span title="decrypted sha256 hash">(.*?)</span>', r.text)
	if match:
		return match.group(1)
	else:
		return None


sock.connect(("hackyeaster.hacking-lab.com", 8888))
awaitMsg(b"Ready for the game?\n")
sendMsg(b"y\n")
awaitMsg(b"Let's go!\n")

digest = readMsg().decode('UTF-8').strip()

while True:
	print("Got digest: %s" % digest)
	cleartext = lookupHash(digest)
	if cleartext:
		print("Found cleartext: %s" % cleartext)
		sendMsg(cleartext.encode('UTF-8') + b'\n')
	else:
		print("Could not determine cleartext")
		sendMsg(b' \n')

	print(">> " + readMsg().decode('UTF-8'))
	score_and_digest = readMsg().decode('UTF-8').strip().split("\n")
	digest = score_and_digest[-1]
	print("\n".join(score_and_digest[:-1]))

sock.close()
