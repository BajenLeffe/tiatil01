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
                      

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')   


os.system('cls')

products = load_data('db_products.csv')

product = get_product_by_id(products, 1)
if product:
    print(f"Found product: {product['name']}")

products = remove_product_by_id(products, 1)

for idx, product in enumerate(products, 1):
    print(f"{idx}. (ID:{product['id']}) {product['name']} {product['desc']} - {format_currency(product['price'])}")