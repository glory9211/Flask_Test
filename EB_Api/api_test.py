import requests

BASE_URL = "http://localhost:5000/"

# Create new User
print()
print("Create new User")
data = {'usr_key': "4938509dsafsad90",
        'subscriptions': ["Netflix", "Amazon"],
        'account_info': "Some Acc Info"
        }
response = requests.put(BASE_URL + 'api/user1', data=data)
print(response.json(), response.status_code)


# Create new User
print()
print("Create new User")
data = {'usr_key': "48789798ERREREafsad90",
        'subscriptions': ["Gym"],
        'account_info': "Some Acc Info"
        }
response = requests.put(BASE_URL + 'api/user2', data=data)
print(response.json(), response.status_code)


# Delete non existant user
print()
print("Delete non existant user")
response = requests.delete(BASE_URL + 'api/user5')
print(response)  # No Data to Return


# Delete existing user
print()
print("Delete existing user")
response = requests.delete(BASE_URL + 'api/user2')
print(response)  # No Data to Return


# Get non existant user
print()
print("Get non existant user")
response = requests.get(BASE_URL + 'api/user5')
print(response.json(), response.status_code)  # No Data to Return

# Get existing user
print()
print("Get existing user")
response = requests.get(BASE_URL + 'api/user1')
print(response.json(), response.status_code)  # No Data to Return
