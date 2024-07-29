# Exemplo Bom

# Calcula a média de notas dos alunos

def calcular_media(notas):
    # Soma todas as notas
    soma = sum(notas)
    # Divide a soma pelo número de notas para obter a média
    media = soma / len(notas)
    return media

# Exemplo de uso da função calcular_media
notas_aluno = [7, 8, 9, 6, 8]
media_aluno = calcular_media(notas_aluno)
print("A média do aluno é:", media_aluno)

# -----------------------------------------
