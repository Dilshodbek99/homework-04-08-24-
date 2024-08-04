from os import system
import json
system("clear")

file = open("product_material.txt", "r")

store = []

str = file.read().split("\n")
print(input("Material nomini kiriting: "))

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

print("Omborda mavjud bo'lgan productlar:")
print("")
for i in range(len(store)):
    store.sort(key=lambda store: store['price'])
    if store[i]['isavailable'] == 'true':
        print(json.dumps(f"Material: {store[i]['material']}, Price: {store[i]['price']}", indent=4))

file.close