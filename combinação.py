def gerar_combinacoes(conjunto, k):
    if k == 0:
        return [[]], 1
    elif len(conjunto) == 0:
        return [], 0
    else:
        combs_sem_item, num_combs_sem_item = gerar_combinacoes(conjunto[1:], k)
        combs_com_item, num_combs_com_item = gerar_combinacoes(conjunto[1:], k-1)
        combs_com_item = [[conjunto[0]] + comb for comb in combs_com_item]
        return combs_sem_item + combs_com_item, num_combs_sem_item + num_combs_com_item

# Define o conjunto de elementos e o tamanho das combinações
conjunto = ['A', 'B', 'C', 'D']
k = 3

# Gera todas as combinações do conjunto e conta o número de combinações geradas
combinacoes, num_combinacoes = gerar_combinacoes(conjunto, k)

# Imprime as combinações geradas e o número de combinações
for c in combinacoes:
    print(c)
print("Número de combinações geradas:", num_combinacoes)
