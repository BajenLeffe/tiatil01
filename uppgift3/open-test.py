import csv
import os
import locale

def format_currency(value):
    return locale.currency(value,grouping=True)

def load_data(filename): 
    products = []
    try:
        with open(filename, encoding='utf-8') as file: 
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    product = {
                        "id": int(row['id']),
                        "name": row['name'],
                        "desc": row['desc'],
                        "price": float(row['price']),
                        "quantity": int(row['quantity'])
                    }
                    products.append(product)
                except ValueError as e:
                    print(f"Error med laddning av rad: {row}. Error: {e}")
    except FileNotFoundError:
        print(f"Error: kunde inte hitta felet {filename}")
    except Exception as e:
        print(f"Error med laddning av data: {e}")
    

    products.sort(key=lambda x: x['id'])
    return products
                    
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls' )

products = load_data('db_products.csv')

for idx, product in enumerate(products, 1):
    print(f"{idx}. (ID:{product['id']}) {product['name']} - {format_currency(product['price'])}")