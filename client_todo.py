import requests

print('[GET] All TODOs')
response = requests.get("http://127.0.0.1:5000/todos")
print(response.status_code)
print(response.json())

print('-----------------------------')

print('[GET] A Specific TODO (id=0)')
response = requests.get("http://127.0.0.1:5000/todos/0")
print(response.status_code)
print(response.json())

print('[GET] A Specific TODO (id=99)')
response = requests.get("http://127.0.0.1:5000/todos/99")
print(response.status_code)
print(response.json())

print('-----------------------------')

print('[POST] Create A TODO')
response = requests.post("http://127.0.0.1:5000/todos",json={'task':'buy milk'})
print(response.status_code)
print(response.json())

print('[GET] All TODOs')
response = requests.get("http://127.0.0.1:5000/todos")
print(response.status_code)
print(response.json())

print('-----------------------------')

print('[DELETE] Remove A TODO (id=2)')
response = requests.delete("http://127.0.0.1:5000/todos/2")
print(response.status_code)


print('[GET] All TODOs')
response = requests.get("http://127.0.0.1:5000/todos")
print(response.status_code)
print(response.json())