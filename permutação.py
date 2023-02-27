def gerar_permutacoes(conjunto):
    if len(conjunto) == 0:
        return [[]], 1
    else:
        permutacoes = []
        num_permutacoes = 0
        for i in range(len(conjunto)):
            item = conjunto[i]
            subconjunto = conjunto[:i] + conjunto[i+1:]
            permutacoes_subconjunto, num_permutacoes_subconjunto = gerar_permutacoes(subconjunto)
            permutacoes_subconjunto = [[item] + permutacao for permutacao in permutacoes_subconjunto]
            permutacoes += permutacoes_subconjunto
            num_permutacoes += num_permutacoes_subconjunto
        return permutacoes, num_permutacoes

# Define o conjunto de elementos
conjunto = ['A', 'B', 'C', 'D']

# Gera todas as permutações do conjunto e conta o número de permutações geradas
permutacoes, num_permutacoes = gerar_permutacoes(conjunto)

# Imprime as permutações geradas e o número de permutações
for p in permutacoes:
    print(p)
print("Número de permutações geradas:", num_permutacoes)
