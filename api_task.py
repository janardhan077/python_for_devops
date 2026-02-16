import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

print("User Names:\n")

users_list = []

for user in data:
    print(user["name"])

    users_list.append({
        "id": user["id"],
        "name": user["name"],
        "email": user["email"]
    })

with open("users.json", "w") as file:
    json.dump(users_list, file, indent=4)

print("\nData saved to users.json")
