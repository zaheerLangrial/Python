import json

x = { "name":"John", "age":30, "city":"New York"}

# parse x:
# y = json.loads(x)

# the result is a Python dictionary:
# print(y["age"])

y = json.dumps(x)
print(y)



x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}


# y = json.loads(x)
print(json.dumps(x))


        # dumps() method is used to convert dict in array
        # and loads() is use to convert array to dict