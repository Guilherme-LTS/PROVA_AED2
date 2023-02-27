def gerar_combinacoes(conjunto, k):
    if k == 0:
        return [[]]
    elif len(conjunto) == 0:
        return []
    else:
        item = conjunto[0]
        combs_sem_item = gerar_combinacoes(conjunto[1:], k)
        combs_com_item = gerar_combinacoes(conjunto[1:], k-1)
        combs_com_item = [[item] + comb for comb in combs_com_item]
        return combs_sem_item + combs_com_item

# Define o conjunto de elementos e o tamanho das combinações
conjunto = ['A', 'R', 'A', 'R', "A"]
k = 2

# Gera todas as combinações do conjunto
combinacoes = gerar_combinacoes(conjunto, k)

# Imprime as combinações geradas
for c in combinacoes:
    print(c)
