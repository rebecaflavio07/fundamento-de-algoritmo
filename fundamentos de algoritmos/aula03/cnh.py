Nascimento= int(input("Digite seu ano de nascimento aqui:"))
Ano=int(input("Digite o ano atual:"))
Idade=(Ano-Nascimento)
if Idade>=18:
    print ("você tem", Idade, "Já pode tirar a CNH, parabéns!")
else:
    print ("você tem", Idade, "poxa não pode tirar a CNH ainda!")

