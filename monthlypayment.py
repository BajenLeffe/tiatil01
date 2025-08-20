def calculate_monthly_payment(principal, annual_rate, years):
    r = (annual_rate / 100) / 12

    n = years * 12

    if r == 0:
        return principal / n 

    A = (principal * r) / (1 - (1 + r) ** -n)
    return A


principal = float(input("Lånebelopp: "))

while True:
    try:
        annual_rate = float(input("Årsränta (%): "))
        break

    except:
        print("did you put in a comma or a period?")

years = int(input("Löptid (år): "))

payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")
