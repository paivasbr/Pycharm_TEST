itens =[]
def adicionar(item):
    itens.append(item)
    print(f'{item} adicionado.')

def remove_item(itemR):
    if itemR in itens:
        itens.remove(itemR)
        print(f"O Item - {itemR} foi removido.")
    else:
        print(f"Não há o Item - {itemR}.")

def mostrar_lista():
    if itens:
        print("Lista de Compras")
        for i, item in enumerate(itens, start=1):
            print(f"{i} - {item}")
    else:
        print("Lista de compras vazia")

while True:
    print("\n1. Adicionar item a lista")
    print("2. Remover item da lista")
    print("3. Ver lista de Compras")
    print("4. Sair")
    escolha = input("Escolha uma opcao (1/2/3/4): ")
    if escolha == "1":
        item = input("Digite um item a ser adicionado: ")
        adicionar(item)
    elif escolha == "2":
        item = input("Digite o item a ser removido: ")
        remove_item(item)
    elif escolha == "3":
        mostrar_lista()
    elif escolha == "4":
        print("Saindo do programa")
        break
    else:
        print("Opção Invalida! Tente Novamente.")
