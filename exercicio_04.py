#codigo para permitir achar o nome do aluno na lista.
nomes=["damon", "stefan", "klaus", "elijah", "katerine"]
pesquisa= input("digite o nome: ")

for x in range(len(nomes)):
    if pesquisa == nomes[x]:
        msg=f"achei o {pesquisa} na posição {x}"
    else:
        msg=f"nome não encontrado"

print(msg)
