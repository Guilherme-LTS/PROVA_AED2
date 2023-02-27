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
        if row == n:
            solucoes.append(rainhas[:])
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
    solucoes = []
    resolver(0)
    return solucoes

# Chama a função para resolver o problema das 8 rainhas
solucoes = resolver_n_rainhas(8)

# Imprime as soluções encontradas
for i, solucao in enumerate(solucoes):
    print("Solução", i+1)
    for linha in range(8):
        linha_str = ""
        for coluna in range(8):
            if solucao[linha] == coluna:
                linha_str += "Q "
            else:
                linha_str += "- "
        print(linha_str)
