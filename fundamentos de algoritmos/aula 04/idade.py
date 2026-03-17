datanasc = int(input("Digite a data de nascimento: "))
ano_atual=int(input("digite o ano atual: "))
idade= ano_atual-datanasc
if idade >=18:
    print("você pode votar e tirar CNH")
elif idade >= 16 and idade < 18:
    print("você pode votar, mas não pode tirar CNH")
else:
    print("você não pode votar e nem tirar CNH")