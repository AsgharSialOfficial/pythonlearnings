
import requests

def fetch_user():
    url = 'https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10'
    response = requests.get(url)
    if response.status_code ==200:
        data = response.json()
        actual_data = data['data']['data']
        return actual_data
    else:
        raise Exception('Failed to fetch users')
    
    
user_list = fetch_user()
print(user_list)
malefound = False
for user in user_list:
    if user['gender']=='male':
        print(f'User Gender: {user['gender']}')
        malefound=True
        break
if not malefound:
    print(f'male is not found')


