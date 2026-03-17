total = 0 #contador
soma = 0 #acumulador

while True:
    x = int(input("digite um valor aqui"))
    if x == 0:
        break
    total +=1
    soma +=x

print(f"Total = {total}\nSoma = {soma}\nMedia = {soma/total}")
