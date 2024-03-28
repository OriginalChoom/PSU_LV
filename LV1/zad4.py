imeTextDat = input("Unesite ime tekst datoteke: ")
file = open(imeTextDat)
totalPouzdanost = 0
brojac = 0
for line in file:
    if (line.startswith("X-DSPAM-Confidence:")):
        pouzdanost = float(line.split(":")[1])
        totalPouzdanost = totalPouzdanost + pouzdanost
        brojac = brojac + 1
file.close()
srednjaVrijednost = totalPouzdanost / brojac
print("Srednja vrijedost pouzdanosti: ", srednjaVrijednost)
