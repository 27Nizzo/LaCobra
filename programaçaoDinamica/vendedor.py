"""

Um vendedor ambulante tem que decidir que produtos levará na sua próxima viagem.
Infelizmente, tem um limite de peso que pode transportar e, tendo isso em atenção, 
tem que escolher a melhor combinação de produtos a transportar dentro desse limite 
que lhe permitirá ter a máxima receita.

Implemente uma função que, dado o limite de peso que o vendedor pode transportar, 
e uma lista de produtos entre os quais ele pode escolher (assuma que tem à sua 
disposição um stock ilimitado de cada produto), devolve o valor de receita máximo
que poderá obter se vender todos os produtos que escolher transportar, e a lista
de produtos que deverá levar para obter essa receita (incluindo repetições, 
caso se justifique), ordenada alfabeticamente.

Cada produto consiste num triplo com o nome, o valor, e o peso.

Caso haja 2 produtos com a mesma rentabilidade por peso deverá dar prioridade 
aos produtos que aparecem primeiro na lista de entrada.

"""

def vendedor(capacidade, produtos):
    return vendedor_aux(capacidade, produtos, {})

def vendedor_aux(capacidade,produtos, memo):
    if capacidade in memo:
        return memo[capacidade]
    if capacidade == 0:
        return 0, []
    r = 0
    lista = []
    for nome, valor, peso in produtos:
        if peso <= capacidade:
            f, l = vendedor(capacidade - peso, produtos)
            if f + valor > r: 
                r = f + valor
                lista = l + [nome]
    memo[capacidade] = r + lista
    lista.sort()
    return r, lista
        