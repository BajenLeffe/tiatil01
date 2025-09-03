from collections import Counter
import csv
import os
import locale

os.system('cls')

def load_sales(filename):
    products = {} 
    all_products = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            product = row['Product']
            sales = float(row['Sales'])
            
            all_products.append(product)
            
            if product in products:
                products[product] += sales
            else:
                products[product] = sales
                
    return all_products, products
                
def analyze_sales_data(all_products, products):    
    # Hittade mest sålda produkten med Counter
    product_counts = Counter(all_products)
    most_sold_product, count = product_counts.most_common(1)[0]
    
    # Hittade mest lukrativa produkten med max och dictionary
    most_lucrative_product = max(products, key=products.get)
    lucrative_amount = products[most_lucrative_product]
    
    print(f"Mest sålda produkt: {most_sold_product}, Antal: {count}")
    print(f"Mest lukrativa produkt: {most_lucrative_product} med försäljning på {locale.currency(lucrative_amount, grouping=True)}")


# Sätt språkinställning till svenska används för att skriva ut formaterad valuta
locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  


all_products, products = load_sales('sales_data.csv')
analyze_sales_data(all_products, products)