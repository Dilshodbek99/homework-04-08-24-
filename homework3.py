from os import system
import json
system("clear")

file = open("product_material.txt", "r")

store = []

str = file.read().split("\n")

for i in range(len(str)):
    str[i] = str[i].split(",")
    str[i][0] = int(str[i][0])
    str[i][3] = float(str[i][3].replace('$', ''))

for i in range(len(str)):
    products = {
        "id": str[i][0],
        "product_code": str[i][1],
        "material": str[i][2],
        "price": str[i][3],
        "isavailable": str[i][4]
    }
    store.append(products)

print("Omborda mavjud bo'lmagan va narxi $1000 kam tovarlar materiallari")
print("")
for i in range(len(store)):
    if store[i]['price'] <= 1000:
        if store[i]['isavailable'] == 'false':
            print(json.dumps(store[i]['material'], indent=4))

file.close