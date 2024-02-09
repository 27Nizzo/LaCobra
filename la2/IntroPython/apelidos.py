'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome).
No caso de pessoas com o mesmo número de apelidos,devem
ser listadas por ordem lexicográfica do nome completo.
'''


def apelidos(nomes):
    nomes.sort(key = lambda y: (len(y.split()), y))
    return nomes
'''
A função apelidos, parece receber uma lista de nomes e, em 
seguida, classifica à base de dois critérios:
-> Comprimento dos Nomes;
-> Ordem Alfabética;
A função ".sort" da lista aceita um argumento "key". O mesmo
é uma função lambda que define como os elementos devem ser 
comparados durante a ordenação.
1) 'len(y.split())': Retorna o comprimento do nome em termos de palavras. 
Isso é utilizado como o primeiro criterio de ordenação.
2) 'y': O nome da função lambda, este é usado com segundo criterio de 
ordenação no caso em que o comprimento seja igual.

Em suma: 
    A função ".sort" irá organizar os nomes consuante o 
    seu comprimento e, em seguida, em ordem alfabética.
'''