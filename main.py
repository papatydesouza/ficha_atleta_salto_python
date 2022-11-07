print("============= FICHA DO ATLETA ==============")
nome = input("Qual o nome do atleta? \n")
saltos = []
media = 0
for i in range(5):
    saltos.append(float(input("Qual a altura do " + str(i+1) + " salto?")))
#print(saltos)

print("****** Resultado Final *******")
print("Atleta: {}" .format(nome))
print("Saltos: {}" .format(saltos))

media = (sum(saltos) / 5)
print("Média: {}" .format(media))

print("****** Fim do Resultado Final ******")