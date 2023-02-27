def gerar_arranjos(conjunto, k):
    if k == 0:
        return [[]], 1
    elif len(conjunto) == 0:
        return [], 0
    else:
        arranjos = []
        num_arranjos = 0
        for i in range(len(conjunto)):
            item = conjunto[i]
            subconjunto = conjunto[:i] + conjunto[i+1:]
            arranjos_subconjunto, num_arranjos_subconjunto = gerar_arranjos(subconjunto, k-1)
            arranjos_subconjunto = [[item] + arranjo for arranjo in arranjos_subconjunto]
            arranjos += arranjos_subconjunto
            num_arranjos += num_arranjos_subconjunto
        return arranjos, num_arranjos

# Define o conjunto de elementos e o tamanho dos arranjos
conjunto = ['A', 'B', 'C', 'D']
k = 4

# Gera todos os arranjos do conjunto e conta o número de arranjos gerados
arranjos, num_arranjos = gerar_arranjos(conjunto, k)

# Imprime os arranjos gerados e o número de arranjos
for a in arranjos:
    print(a)
print("Número de arranjos gerados:", num_arranjos)
