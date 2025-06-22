"""
digitar uma lista de numeros separados por espaço e usar o filter() para encontrar pares
"""

def pares_numeros():
    lista_string_input = input("digite uma lista separado por espaço: ")
    lista_valores = [int(valor) for valor in lista_string_input.split()]
    lista_pares = list(filter(lambda x: x%2==0, lista_valores))
    print(lista_pares)


pares_numeros()