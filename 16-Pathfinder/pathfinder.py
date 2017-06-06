import requests

ua_pathfinder = {'User-Agent': 'PathFinder'}
base_url = "http://hackyeaster.hacking-lab.com:9999/"

def visit_path(curr_path):
	url = base_url + "".join([str(x) for x in curr_path])
	print("Visiting: %s" % url)
	r = requests.get(url, headers=ua_pathfinder)
	res_json = r.json()
	if res_json['Answer'] == r"You've left the path!":
		return False
	elif res_json['Answer'] == r"This leads to nowhere, so turn around!":
		return False
	elif 'paths' in res_json:
		for p in res_json['paths']:
			req_res = visit_path(curr_path + [p])
			if req_res:
				return req_res
	else:
		return res_json


print(visit_path([]))

