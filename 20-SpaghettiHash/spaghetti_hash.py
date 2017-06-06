import hashlib
import requests
import os.path

LARRY_HASH_URL = "https://hackyeaster.hacking-lab.com/hackyeaster/hash"

PASSWORD_HASHES = [
    "87017a3ffc7bdd5dc5d5c9c348ca21c5",
    "ff17891414f7d15aa4719689c44ea039",
    "5b9ea4569ad68b85c7230321ecda3780",
    "6ad211c3f933df6e5569adf21d261637"
]

def lookup_larry_hash(cleartext):
    res = requests.get(LARRY_HASH_URL, params={'string':cleartext})
    return res.text


def sha512(cleartext):
    return hashlib.sha512(cleartext.encode()).hexdigest()


def larry_hash(sha512_digest, index_map):
    return "".join([sha512_digest[idx] for idx in index_map])


def main():
    print("Determening pattern...")
    
    # List of sets, where each set holds the possible indices 
    # in the sha512 digest that goes into that position in 
    # the larry hash.
    index_map = [set(range(128)) for _ in range(32)]
    i = 0
    while True:
        cleartext = str(i)
        i += 1
        larry_digest = lookup_larry_hash(cleartext)
        sha512_digest = sha512(cleartext)
        print("Testing: %s" % cleartext)
        
        for pos, char in enumerate(larry_digest):
            sha512_indices = [i for i, x in enumerate(sha512_digest) if x == char]
            index_map[pos] &= set(sha512_indices)
        
        # Check if we have a single mapping for each position,
        # in which case we are done
        if all([len(x) == 1 for x in index_map]):
            break

    # list of sets -> list of one index per position
    index_map = [x.pop() for x in index_map]
    print("Index pattern found!")
    print(", ".join(["%d -> %d" % (idx, pos) for pos, idx in enumerate(index_map)]))

    if not os.path.isfile('rockyou.txt'):
        print("We need that rockyou.txt wordlist...")
        print("https://wiki.skullsecurity.org/Passwords")
        return
    
    print("Cracking passwords...")
    with open('rockyou.txt', encoding="latin-1") as pass_file:
        for password in pass_file:
            password = password.rstrip()
            larry_digest = larry_hash(sha512(password), index_map)
            for h in PASSWORD_HASHES[:]:
                if larry_digest == h:
                    print("%s == %s" % (h, password))
                    PASSWORD_HASHES.remove(h)
            if not PASSWORD_HASHES:
                break 


if __name__ == '__main__':
    main()
