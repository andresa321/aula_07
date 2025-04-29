#codigo para ler nota de uma turma de 5 alunos.
notas=[""]*5
soma=0
contador=0
#codigo for para calcular notas
for x in range(len(notas)):
    notas[x]= float(input("digite a nota: "))
    soma = soma + notas[x]
#variavel para media
media = soma/len(notas)
#for para saber se notas é maior que media
for x in range(len(notas)):
    if notas[x] > media:
        contador += 1

print(f"a media dos alunos da turma foi {media} e quantidade de alunos com a nota maior que a media foi {contador}")

