import csv
import os
import locale
from colors import bcolors

def format_currency(value):
    return locale.currency(value,grouping=True)

def load_data(filename): 
    products = []
    
    with open(filename, encoding='utf-8', mode='r') as file: 
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
    
    # ta reda på högsta ID och lägg till 1
    new_id = max(products, key=lambda x: x['id'])['id'] + 1
    
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
    try:
        fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
        
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(products)
        return True
    
    except:
        print("\nFEL: kan inte spara - filen är skrivskyddad")
        return False

def show_products(products):
    print(f"\n{bcolors.BOLD}Aktuell produktlista:{bcolors.DEFAULT}\n")

    for idx, product in enumerate(products, 1):
        print(f"{bcolors.BLUE}{idx}. {bcolors.DEFAULT}(ID:{bcolors.YELLOW}{product['id']}{bcolors.DEFAULT}) "
              f"{bcolors.CYAN}{product['name']} {product['desc']}{bcolors.DEFAULT} - "
              f"{bcolors.GREEN}{format_currency(product['price'])}{bcolors.DEFAULT} "
              f"({bcolors.PURPLE}{product['quantity']}{bcolors.DEFAULT} st)")

locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')   


filename = 'db_products.csv'
products = load_data(filename)

while True:
    os.system('cls')
    show_products(products)
    
    print(f"\n{bcolors.BOLD}välj en åtgärd:{bcolors.DEFAULT}")
    print("1. sök produkt via ID")
    print("2. ta bort produkt")
    print("3. lägg till produkt")
    print("4. avsluta")
    
    choice = input(f"\n{bcolors.CYAN}välj (1-4): {bcolors.DEFAULT}")
    
    if choice == '1':
        try:
            product_id = int(input(f"\n{bcolors.CYAN}ange ID på produkten du söker: {bcolors.DEFAULT}"))
            product = get_product_by_id(products, product_id)

            if product:
                print(f"\n{bcolors.GREEN}hittade produkt: {product['name']} {product['desc']} - {format_currency(product['price'])}{bcolors.DEFAULT}")
            else:
                print(f"\n{bcolors.RED}ingen produkt hittades med ID {product_id}{bcolors.DEFAULT}")
        except:
            print(f"\n{bcolors.RED}ogiltigt ID format{bcolors.DEFAULT}")

    elif choice == '2':
        try:
            product_id = int(input(f"\n{bcolors.CYAN}ange ID på produkten du vill ta bort: {bcolors.DEFAULT}"))
            old_len = len(products)
            products = remove_product_by_id(products, product_id)

            if len(products) < old_len:
                print(f"\n{bcolors.GREEN}produkt med ID {product_id} har tagits bort{bcolors.DEFAULT}")
                if not save_data(filename, products):
                    print(f"{bcolors.RED}ändringen kommer inte sparas nästa session{bcolors.DEFAULT}")
            else:
                print(f"\n{bcolors.RED}ingen produkt hittades med ID {product_id}{bcolors.DEFAULT}")
        except:
            print(f"\n{bcolors.RED}ogiltigt ID format{bcolors.DEFAULT}")

    elif choice == '3':
        products = add_product(products)
        if not save_data(filename, products):
            print(f"{bcolors.RED}ändringen kommer inte sparas nästa session{bcolors.DEFAULT}")

    elif choice == '4':
        print(f"\n{bcolors.YELLOW}avslutar programmet...{bcolors.DEFAULT}")
        break

    else:
        print(f"\n{bcolors.RED}ogiltigt val, försök igen{bcolors.DEFAULT}")

    input(f"\n{bcolors.CYAN}tryck Enter för att fortsätta...{bcolors.DEFAULT}")
