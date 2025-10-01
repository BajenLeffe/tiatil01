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

def save_data(filename, products):
    fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

def show_products(products):
    print("\nAktuell produktlista:\n")
    for idx, product in enumerate(products, 1):
        print(f"{idx}. (ID:{product['id']}) {product['name']} {product['desc']} - {format_currency(product['price'])}")

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')   


filename = 'db_products.csv'
products = load_data(filename)

while True:
    os.system('cls')
    show_products(products)
    
    print("\nvälj en åtgärd:")
    print("1. sök produkt via ID")
    print("2. ta bort produkt")
    print("3. lägg till produkt")
    print("4. avsluta")
    
    choice = input("\nvälj (1-4): ")
    
    if choice == '1':
        try:
            product_id = int(input("\nange ID på produkten du söker: "))
            product = get_product_by_id(products, product_id)
            if product:
                print(f"\nhittade produkt: {product['name']} {product['desc']} - {format_currency(product['price'])}")
            else:
                print(f"\ningen produkt hittades med ID {product_id}")
        except ValueError:
            print("\nogiltigt ID format")
    
    elif choice == '2':
        try:
            product_id = int(input("\nange ID på produkten du vill ta bort: "))
            old_len = len(products)
            products = remove_product_by_id(products, product_id)
            if len(products) < old_len:
                print(f"\nprodukt med ID {product_id} har tagits bort")
                save_data(filename, products)
            else:
                print(f"\ningen produkt hittades med ID {product_id}")
        except ValueError:
            print("\nogiltigt ID format")
    
    elif choice == '3':
        products = add_product(products)
        save_data(filename, products)
    
    elif choice == '4':
        print("\navslutar programmet...")
        break
    
    else:
        print("\nogiltigt val, försök igen")
    
    input("\ntryck Enter för att fortsätta...")
