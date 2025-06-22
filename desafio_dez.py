"""
digite  uma função que faz calculo de soma recursivo até o valor digitado
"""
valor = int(input("Digite um  valor inteiro para somar de 1 até: "))

def soma(n):
    if n <= 1 :
        return 1
    else:
        return n + soma(n - 1)
valor_novo = soma(valor)

print(f"A soma dos valores é {valor_novo}")