"""
uma função que calcule o desconto de porcentagem de uma compra
"""

compra = float(input("Digite o valor da sua compra: "))
desconto = float(input("Digite a porcentagem do desconto ex: (10% = 0.1): "))

resultado = lambda compra, desconto: compra - (compra * desconto)
print(resultado(compra, desconto))
