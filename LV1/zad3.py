import statistics

listaBrojeva = []
broj = input()
unesenoBrojeva = 0
try: 
    while broj != "Done":
        if(broj.isdigit):
            unesenoBrojeva = unesenoBrojeva + 1
            listaBrojeva.append(broj)
        broj = input()
except ValueError:
    print("Ne moze slova")

print(listaBrojeva)
print("Uneseno je: ", unesenoBrojeva)
mid = statistics.median(listaBrojeva)
print("Srednja vrijednost je: ", mid)
print("Maksimalna vrijednost je:", max(listaBrojeva))
print("Minimalna vrijednost je: ", min(listaBrojeva))