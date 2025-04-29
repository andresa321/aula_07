#preencher vetor A com 5 numeros
A=[5,6,7,8,9]
x=int(input("digite o numero: "))

M=[""]*5

for i in range(len(A)):
    M[i]=A[i]*x

print(f"{A}\n {x}\n {M}\n")