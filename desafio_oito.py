"""
crie uma calculadora que o usuario digita dois  numeros e escolhe a operação
"""
def soma(a, b) -> float:
    return a + b
def subtracao(a, b) -> float:
    return a - b
def divisao(a, b) -> float:
    try:
        resultado = a/b
    except ZeroDivisionError as e:
        print(f"Não pode ter divisão por zero!")
    else:
        return resultado
def multitplicacao(a, b) -> float:
    return a * b

def calculadora():
    primeiro = float(input("Digite o primeiro valor: "))
    segundo = float(input("Digite o segundo valor: "))
    resultado = 0
    print("Digite a operacao que deseja")
    print("Soma: +")
    print("Subtração: - ")
    print("Multiplicação: *")
    print("Divisao: /")
    operacao = input("Qual deseja:")
    if operacao == "+" or operacao == "Soma":
        resultado = soma(primeiro, segundo)
    elif operacao == "-" or operacao == "Subtração":
        resultado = subtracao(primeiro, segundo)
    elif operacao == "*" or operacao == "Multiplicação":
        resultado = multitplicacao(primeiro, segundo)
    elif operacao == "/" or operacao == "Divisão":
        resultado = divisao(primeiro, segundo)
    else:
        print("Operação invalida!")
    print(resultado)

calculadora()


