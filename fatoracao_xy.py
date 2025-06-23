
# -*- coding: utf-8 -*-

'''
Favor, fazer uma branch separada para implementar o calculo que está restando
Após isso, nós testamos e vemos a melhor versão, depois daremos merge
'''

# 
# Verificar quando a divisão é por zero (não sei onde tem divisão nessa porra) P: Nem Eu
# Fazer o calculo das matriz upper e lower e retorna-las a main
# Fazer o calculo na função calculate_lu
#

def show(matrix, size):
    for i in range(size):
        for n in range(size):
            print(f'{matrix:.2f}', end='\t')
        print()
    
# Fazer o calculo aqui
def calculate_lu(matriz, size):
    upper_matriz, lower_matriz = make_matrices(size)
    
    
    
    for k in range(size):
        for j in range(k, size):
            soma = 0
            for s in range(k):
                soma += lower_matriz[k][s] * upper_matriz[s][j]
            upper_matriz[k][j] = matriz[k][j] - soma    
        for i in range(k+1, size):
            soma = 0
            for s in range(k):
                soma += lower_matriz[i][s] * upper_matriz[s][k]
                
            
            pivo = upper_matriz[k][k]
            if pivo == 0:
                raise ZeroDivisionError(f"Divisão por zero no pivô U[{k}][{k}]")

            lower_matriz[i][k] = (matriz[i][k] - soma) / pivo

    
    
    
    return upper_matriz, lower_matriz
    
def make_matrices(size: int):
    return [[0] * size for _ in range(size)], [[1 if i == n else 0 for i in range(size)] for n in range(size)]

def main():
    size = int(input())    
    matriz = [list(map(float, input().split())) for _ in range(size)]
    upper_matrix, lower_matrix = calculate_lu(matriz, size)

    show(upper_matrix, size)
    show(lower_matrix, size)

    return 0
    
main()
