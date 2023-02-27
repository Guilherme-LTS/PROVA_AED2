def resolver_n_rainhas(n):
    def checar_diagonal_principal(row, col):
        return row - col not in diagonais_principais
    
    def checar_diagonal_secundaria(row, col):
        return row + col not in diagonais_secundarias
    
    def checar_coluna(row, col):
        return col not in colunas
    
    def adicionar_rainha(row, col):
        rainhas[row] = col
        colunas.add(col)
        diagonais_principais.add(row - col)
        diagonais_secundarias.add(row + col)
        
    def remover_rainha(row, col):
        rainhas[row] = -1
        colunas.remove(col)
        diagonais_principais.remove(row - col)
        diagonais_secundarias.remove(row + col)
    
    def resolver(row):
        nonlocal num_solucoes
        if row == n:
            num_solucoes += 1
            return
        
        for col in range(n):
            if checar_coluna(row, col) and checar_diagonal_principal(row, col) and checar_diagonal_secundaria(row, col):
                adicionar_rainha(row, col)
                resolver(row + 1)
                remover_rainha(row, col)
    
    rainhas = [-1] * n
    colunas = set()
    diagonais_principais = set()
    diagonais_secundarias = set()
    num_solucoes = 0
    resolver(0)
    return num_solucoes

# Chama a função para resolver o problema das 8 rainhas
num_solucoes = resolver_n_rainhas(8)

# Imprime o número de soluções encontradas
print("Número de soluções:", num_solucoes)
