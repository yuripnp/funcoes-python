"""
converter numeros de telefone de strings para inteiros
"""


telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 
converter = lambda numero: int(numero)
lista_convertida = [converter(numero) for numero in telefones]
print(lista_convertida)
print(telefones)