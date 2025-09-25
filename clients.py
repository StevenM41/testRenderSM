import requests
code=41000
URL=f"http://localhost:8000/code-postal/{code}"

response = requests.get(URL)

print(response.status_code)
print(response.json())
