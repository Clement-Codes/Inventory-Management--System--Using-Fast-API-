import requests

#print(requests.get("http://127.0.0.1:8000/").json())
print(requests.get("http://127.0.0.1:8000/items?name=Nails").json())

host = "http://127.0.0.1:8000/"
print("Adding an item:")
print(
    requests.post(f"{host}",
                  json={"name":"Screwdriver", "price": 3.99, "count": 10, "id": 4, "category":"tools"},
                  ).json()
)

print("Updating an item:")
print(requests.put(f"{host}items/0?count=9001").json())
print(requests.get(f"{host}").json())

print("Updating an item:")
print(requests.delete(f"{host}items/4").json())
print(requests.get(f"{host}").json())
