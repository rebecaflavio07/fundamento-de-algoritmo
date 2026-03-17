altura=float(input("Digite a altura da pessoa: "))
sexo=input("digite o sexo da pessoa (M/F):")

if sexo=='F':
    peso_ideial= (62.1*altura) -44.7
    print(f"Seu peso ideal é {peso_ideial:.2f} kg")
elif sexo=='M':
    peso_ideial= (72.7*altura)-58.7
    print(f"Seu peso ideal é {peso_ideial:.2f} kg")
else:
    print("sexo inválido")