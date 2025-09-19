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
                    
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls')

products = load_data('db_products.csv')

for idx, product in enumerate(products, 1):
    print(f"{idx}. (ID:{product['id']}) {product['name']} {product['desc']} - {format_currency(product['price'])}")