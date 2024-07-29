# EXEMPLO BOM

# Implementação com uma função

def calcular_media(lista_medias):
    soma_media = sum(lista_medias)
    media_final = soma_media / len(lista_medias)
    return media_final

# Agora podemos chamar esta função sempre que precisarmos calcular a média de uma lista
lista = [10, 20, 30, 40, 50]
media = calcular_media(lista)
print("Média da lista:", media)

outra_lista = [15, 25, 35, 45, 55]
media_outra = calcular_media(outra_lista)
print("Média da outra lista:", media_outra)

# -----------------------------------------