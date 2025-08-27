import os

os.system('cls')

def räkna_ut_betalning(belopp, årsränta, år):
    r = (årsränta / 100) / 12

    n = år * 12

    if r == 0:
        return belopp / n 

    A = (belopp * r) / (1 - (1 + r) ** -n)
    return A
u

belopp = float(input("Lånebelopp: "))

while True:
    try:
        årsränta = float(input("Årsränta (%): "))
        break

    except:
        print("lade du in ett komma eller punkt?")

år = int(input("Löptid (år): "))

betalning = räkna_ut_betalning(belopp, årsränta, år)
print(f"Din månatliga betalning är: {betalning:.2f} kr")
