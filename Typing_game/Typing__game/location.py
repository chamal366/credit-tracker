import requests
response = requests.get("https://ipinfo.io/json").json()

print(f"City: {response['city']}")
print(f"Region: {response["region"]}")
print(f"Country: {response['country']}")