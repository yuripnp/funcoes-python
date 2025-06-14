
def ola_mundo(nome):
    return f"olá {nome}"

def soma(a, b):
    soma = a + b
    return soma

def comprimento(nome = "visitante"):
    print(f"Olá {nome}")

comprimento() # imprime olá visitante
comprimento("yuri") # imprime olá yuri

#--- funções recursivas ---
#são aquelas funções que chamam a si mesmas para resolver problemas repetitivos até atingir uma condição
#de parada
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n -1)

#-- funções lambdas --
#são aquelas funções que são pequenas, sem nome e que podem ter multiplos argumentos, mas apenas uma expressao
# lambda argumentos: expressao
soma = lambda a, b, c: a + b + c
print(soma(1, 2, 3))

# -- funções que trabalham com iteraveis --
# filter(operacao, iteravel) Filtra elementos de um iteravel com base uma condição
print(list(filter(lambda x: x > 2, [1,2,3,4])))
# map(funcao, iteravel) # aplica uma função para cada elemento iteravel
print(list(map(lambda x: x*2, [1, 2, 3])))
# zip(iteravel1, iteravel2, ...) # Une dois ou mais iteraveis, criando pares de elementos correspondentes
print(list(zip([1,2,3],["a","b","c"],[True, False, False])))
# sorted(iteravel, key=funcao, reverse=bool) # retorna uma nova lista  retornada apartir do iteravel. Pode
# receber um argumento key para personalizar a ordenação
print(list(sorted([1,2,3,6,4,9,3])))
print(list(sorted(["abacaxi","cenoura","bolo","melancia"], key=len)))

