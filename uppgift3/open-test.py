import csv
import os
import locale

def format_currency(value):
    return locale.currency(value,grouping=True)

def load_data(filename): 
    products = []  # Flytta produkter in till listan
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(
                {                   
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products

def get_product_by_id(products, product_id):
    
    for product in products:
        if product['id'] == product_id:
            return product
    return None

def remove_product_by_id(products, product_id):
    
    for i, product in enumerate(products):
        if product['id'] == product_id:
            return products.pop(i)
    return None

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

products = load_data('db_products.csv')  # Laddar in hela CSV filen

os.system('cls')

for idx, product in enumerate(products, 1):
    print(f"{idx}. {product['name']} - {format_currency(product['price'])}")