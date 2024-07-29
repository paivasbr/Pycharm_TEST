"""
- Desafio: Calculadora simples.
- Requisitos Técnicos: Laços de repetição, condicionais, entrada e saída de dados, operações matemáticas, coleções de dados.
- Descrição Geral: Desenvolva um aplicativo de calculadora que funcione via linha de comando (terminal).
O usuário deve ser capaz de escolher entre diferentes operações matemáticas, inserir números para realizar os cálculos, e navegar no menu do aplicativo.

Requisitos Funcionais:
Menu principal:

Calculadora Simples

1. Soma
2. Subtração
3. Multiplicação
4. Divisão
5. Sair

Deve escolher a operação utilizando os números referentes à opção do menu e apertar ENTER.
Uma vez escolhida a operação, a aplicação deverá solicitar dois números e executar a aoperação selecionada sobre eles.
IMPORTANTE!! Precisamos nos atentar às divisões por zero!

Entrada:
"Primeiro número:"
"Segundo número:"

Saída:
O resultado da [OPERAÇÃO SELECIONADA] é: [RESULTADO]
Ex. "O resultado da operação soma é: 42"

Quando a operação for finalizada, deverá voltar ao menu principal.
Se o usuário pressionar s, o aplicativo deverá agradecer o usuário e sair.
"""

def calculadora():
    while True:
        print("Calculadora Simples")
        print()
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")
        operacao = input("selecione uma opção ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print("Obrigado(a) por utilizar a calculadora simples!")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue

        numero_1 = float(input("Primeiro número: "))
        numero_2 = float(input("Segundo número: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("O resultado da operação soma é: ", resultado)
        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("O resultado da operação subtração é: ", resultado)
        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("O resultado da operação multiplicação é: ", resultado)
        else:
            if numero_2 == 0:
                print("Divisões por zero não são possíveis. Tente novamente.")
                continue
            else:
                resultado = numero_1 / numero_2
                print("O resultado da orperação divisão é: ", resultado)

calculadora()


