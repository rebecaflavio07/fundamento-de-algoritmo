numero_1= int(input("digite o primeiro numero"))
numero_2= int(input("digite o segundo numero"))
numero_3= int(input("digite o terceiro numero"))
if numero_1 < numero_2 and numero_1 < numero_3:
    print(f"o numero {numero_1} é o menor")
elif numero_2 < numero_1 and numero_2 < numero_3:
    print(f"o numero {numero_2} é o menor")
else:
    print(f"o numero {numero_3} é o menor")
