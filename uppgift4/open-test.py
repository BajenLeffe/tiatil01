import csv
import os
import locale

def format_currency(value):
    return locale.currency(value,grouping=True)

def load_data(filename): 
    products = []
    with open(filename, encoding='utf-8') as file: 
        reader = csv.DictReader(file)
        for row in reader:
                product = {
                    "id": int(row['id']),
                    "name": row['name'],
                    "desc": row['desc'],
                    "price": float(row['price']),
                    "quantity": int(row['quantity'])
                }
                products.append(product)
    
    products.sort(key=lambda x: x['id'])
    return products

def get_product_by_id(products, product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return None

def remove_product_by_id(products, product_id):
    new_products = []
    for product in products:
        if product['id'] != product_id:
            new_products.append(product)
    return new_products


def add_product(products):
    print("\nlägg till en ny produkt")

    findmax = max(products, key=lambda biggest: biggest['id'])
    new_id = findmax['id'] + 1 
    
    new_name = input("ange produktens namn: ")
    new_desc = input("ange produktens beskrivning: ")
    new_price = float(input("ange produktens pris: "))
    new_quantity = int(input("ange produktens antal: "))

    new_product = {
        "id": new_id,
        "name": new_name,
        "desc": new_desc,
        "price": new_price,
        "quantity": new_quantity
    }
    products.append(new_product)
    products.sort(key=lambda x: x['id'])
    print(f"\nprodukten '{new_name}' har lagts till!\n")
    return products

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')   


os.system('cls')

products = load_data('db_products.csv')

product_id_to_get = int(input("ange ID på produkten du söker: "))
product = get_product_by_id(products, product_id_to_get)
if product:
    print(f"hittade produkt med ID {product_id_to_get}: {product['name']} {product['desc']} - {format_currency(product['price'])}")
else:
    print(f"ingen produkt hittades med detta ID {product_id_to_get}")


product_id_to_remove = int(input("\nange ID på produkten du vill bli av med: "))
products = remove_product_by_id(products, product_id_to_remove)

print("\ndatabasen med produkten borttagen:\n")
for idx, product in enumerate(products, 1):
    print(f"{idx}. (ID:{product['id']}) {product['name']} {product['desc']} - {format_currency(product['price'])}")

choice = input("\nvill du lägga till en ny produkt? (y/n): ").lower()
if choice == 'y':
    products = add_product(products)

print("\nslutgiltig produktlista:\n")
for idx, product in enumerate(products, 1):
    print(f"{idx}. (ID:{product['id']}) {product['name']} {product['desc']} - {format_currency(product['price'])}")
