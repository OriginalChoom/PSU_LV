print("Ocjena izmedu 0.0 i 1.0")

try:
    ocjena = float(input())  
    if(ocjena > 1.0 or ocjena < 0.0):
        print("Izvan intervala")
    if(ocjena >= 0.9):
        print("A")
    elif(ocjena >= 0.8):
        print("B")
    elif(ocjena >= 0.7):
        print("C")
    elif(ocjena >= 0.6):
        print("D")
    else:
        print("F")
except ValueError:
        print("Nije broj")