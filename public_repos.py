import requests
import sys

if len(sys.argv) >= 2:
    user_name = sys.argv[1]
else:
    print("Error: username missing in argument")
    sys.exit(0)

endpoint = 'https://api.github.com/users/' + user_name + '/repos'

# print(endpoint)
content = requests.get(endpoint).json()

if 'message' in content and content['message'] == 'Not Found':
    print("Error: Not a valid username")
    sys.exit(0)

if len(content) == 0:
    print("No repos found for user " + user_name)
    sys.exit(0)

for repo in content:
    print(repo['full_name'])
