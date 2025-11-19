# Verifica se uma palavra é um palíndromo

palavra = input("Digite uma palavra: ")

invertida = palavra[::-1]

if palavra == invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' NÃO é um palíndromo.")
