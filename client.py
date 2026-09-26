import requests

response = requests.get("http://localhost:8000/api/users/123")

print("Status Code:", response.status_code)
print("Response:", response.json())
