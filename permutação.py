def gerar_permutacoes(conjunto):
    if len(conjunto) == 0:
        return [[]]
    else:
        permutacoes_anteriores = gerar_permutacoes(conjunto[1:])
        novas_permutacoes = []
        for p in permutacoes_anteriores:
            for i in range(len(p)+1):
                nova_permutacao = p[:i] + [conjunto[0]] + p[i:]
                novas_permutacoes.append(nova_permutacao)
        return novas_permutacoes

# Define o conjunto de elementos
conjunto = ['A', 'B', 'C', "D"]

# Gera todas as permutações do conjunto
permutacoes = gerar_permutacoes(conjunto)

# Imprime as permutações geradas
for p in permutacoes:
    print(p)
