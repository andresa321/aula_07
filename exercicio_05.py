#codigo para ler nota de uma turma de 5 alunos.
notas=[""]*5
soma=0
contador=0
#codigo for para calcular notas, guardar valores dentro do arrey
for x in range(len(notas)):
    notas[x]= float(input("digite a nota: "))
    soma = soma + notas[x]
#variavel para media tem que ser fora
media = soma/len(notas)
#for para verificar se notas na posição tal é maior que a media
for y in range(len(notas)):
    if notas[y] > media:
        contador += 1

print(f"a media dos alunos da turma foi {media} e quantidade "
      f"de alunos com a nota maior que a media foi {contador}")