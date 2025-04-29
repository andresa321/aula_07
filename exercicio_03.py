#codigo para alterar o exercicio anterior para adicionar os 5 nomes e dizer a posicao deles.
nomes = [""]*5

for x in range(5):
    nomes[x]=input("digite o nome: ")

for j in range(len(nomes)):
    print(nomes[j], j)