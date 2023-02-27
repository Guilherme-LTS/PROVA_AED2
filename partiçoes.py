def gerar_particoes(conjunto, k):
    if k == 1:
        return [[conjunto]], 1
    if len(conjunto) == k:
        return [[ [x] for x in conjunto ]], 1
    particoes = []
    num_particoes = 0
    for i in range(1, len(conjunto) - k + 2):
        subparticoes, num_subparticoes = gerar_particoes(conjunto[i:], k - 1)
        num_particoes += num_subparticoes
        for subparticao in subparticoes:
            particao = [[conjunto[:i]]] + subparticao
            particoes.append(particao)
            num_particoes += 1
    return particoes, num_particoes

# Define o conjunto de elementos e o número de subconjuntos
conjunto = ['A', 'B', 'C', 'D', 'E']
k = 3

# Gera todas as partições do conjunto em k subconjuntos e conta o número de partições geradas
particoes, num_particoes = gerar_particoes(conjunto, k)

# Imprime as partições geradas e o número de partições
for particao in particoes:
    print(particao)
print("Número de partições geradas:", num_particoes)
