# lista_de_compras = ["Ovos", "Farinha", "Leite", "Confete", "Arroz", "Chantili"]
#
# for item in lista_de_compras:
#     print("Comprei o item:", item)

## Control + / (Comenta todos os itens selecionados);

numero = 0;

while True:
    print("Número", numero)
    numero = numero + 1

    if numero % 2 == 0: # Forma de verificar se o número é par
        print(numero, "é par")
        continue

    print(numero, "é impar")