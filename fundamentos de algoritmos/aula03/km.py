km=int(input("Quantos km você deseja percorrer?"))
if km<=200:
    valor=(km*0.50)
    print("você deve pagar R$", valor, )

if km>200:
    total=(km*0.45)
    print("você deve pagar um valor de R$" , total,)