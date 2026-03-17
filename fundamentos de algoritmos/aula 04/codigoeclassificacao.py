codigo=int(input("Digite um código: "))
if codigo==1:
    print("Alimento não-perecível")
elif codigo==2:
    print("Alimento perecível")
elif codigo>=3 and codigo<=5:
    print("Vestuário")
elif codigo==7:
    print("Higiene pessoal")
elif codigo >=8 and codigo<=15:
    print("Utensílios domésticos")
else:
    print("Código inválido")