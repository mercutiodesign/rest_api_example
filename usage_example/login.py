import requests
from getpass import getpass

session = requests.Session()
url = "http://localhost:8000/api/api-auth/login/"
session.head(url).raise_for_status()
session.headers = {'X-CSRFToken': session.cookies['csrftoken']}
payload = {'username': input('username: '), 'password': getpass('password (hidden): ')}
session.post(url, data=payload).raise_for_status()
print('logged in:', 'sessionid' in session.cookies)
