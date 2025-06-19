"""
converter uma lista de valores inseridos em uma linha e somalos
"""

def digitar_valores():
    valores_unico =  input("Digite os gastos: ")
    soma = 0
    try:
        valores = valores_unico.split()
        for valor in valores:
            valor_convertido = float(valor)
            soma = soma + valor_convertido
    except ValueError as e:
        print(f"valor incorreto {e}")
    else:
        print(soma)

digitar_valores()