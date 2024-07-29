# EXEMPLO BOM

# Função para clacular a média de uma lista de números

def calcular_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

# Função para determinar se um aluno foi aprovado

def verificar_aprovacao(media):
    if media >= 6.0:
        return True
    else:
        return False

# Lista de notas de um aluno
notas_aluno = [7, 8, 9, 6, 8]

# Calcula a média do aluno
media_aluno = calcular_media(notas_aluno)

# Verificar se o aluno foi aprovado
aprovado = verificar_aprovacao(media_aluno)

# Exibe o resultado
if aprovado:
    print("O aluno foi aprovado!")
else:
    print("O aluno foi reprovado")

# ---------------------------------