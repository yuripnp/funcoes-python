import datetime
"""
crie um programa que calcule o ano de nascimento com o atual e de a ideade
"""

def idade(data_de_nascimento: int) -> int:
    """atraves do ano de nascimento, 
    retornamos a idade"""
    try:
        ano_atual = int(datetime.date.today().year)
        idade = ano_atual - data_de_nascimento
    except ValueError as e:
        print(f"data de nascimento invalida")
    else:
        return idade
print(idade(1992))