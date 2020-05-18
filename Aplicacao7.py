numeros = input().split()

maior = 0
menor = 999999
soma = 0

for i in range(len(numeros)):
    numeros[i] = int(numeros[i])
    if numeros[i] > maior:
        maior = numeros[i]
    if numeros[i] < menor:
        menor = numeros[i]
    soma += numeros[i]

print(maior, menor, soma)
