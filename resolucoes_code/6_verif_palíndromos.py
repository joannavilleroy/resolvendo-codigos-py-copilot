# Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

palavra = input("Vamos testar se uma palavra é um palíndromo?! Digite a palavra para verificarmos: ")

invertida = palavra[::-1]

if palavra == invertida:
    print("Essa palavra é um palíndromo")
else:
    print("Essa palavra não é um palíndromo, invertida ela fica assim '{}'".format(invertida))