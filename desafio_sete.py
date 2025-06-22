"""
digite duas listas de produtos e preços e depois junte essas listas em tuplas
"""

produtos = input("Digite os produtos separados por virgula: ")
precos = input("Digite os valores dos produtos: ")

def produtos_precos(produtos, precos):
    produtos_precos = {}
    try:
        lista_produtos = produtos.split(",")
        lista_precos = precos.split()
        lista_precos = [valor.strip() for valor in lista_precos]
        lista_produtos = [valor.strip() for valor in lista_produtos]
        if len(lista_precos) != len(lista_produtos):
            raise Exception(f"erro, listas não são iguais!")
        for i in range(len(lista_produtos)):
            produtos_precos[lista_produtos[i]] = lista_precos[i]
        print(produtos_precos)
    except ValueError as e:
        print("valor invalido {e}")
    else:
        print(produtos_precos)
produtos_precos(produtos, precos)
