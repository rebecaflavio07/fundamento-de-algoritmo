preco=float(input("digite o preço do produto"))
codigo=int(input("digite o valor do produto aqui"))

if  codigo ==1:
    procedencia="sul"
elif codigo ==2:
    procendencia="norte"
elif codigo ==3:
    procedencia="leste"
elif codigo ==4:
    procendencia="oeste"
elif codigo ==5 or codigo ==6:
    procendencia="nordeste"
elif 7 <= codigo <= 9:
    procedencia="sudeste"
elif 10<= codigo <= 20:
    procedencia="centro-oeste"   
elif 25<= codigo <=30:
    procedencia="nordeste"
else:
    procedencia="importado"

print (f"Preço: R${preco:.2f} - Procedência: {procedencia}")