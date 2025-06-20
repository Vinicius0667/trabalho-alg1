# -*- coding: utf-8 -*-

# 
# Verificar quando a divisão é por zero (não sei onde tem divisão nessa porra)
# Fazer o calculo das matriz upper e lower e retorna-las a main
# Fazer o calculo na função calculate_lu
#

def show(matrix, size):
    for i in range(size):
        for n in range(size):
            print(f'{matrix:.2f}', end='\t')
        print()
    
# Terminar o calculo aqui
def calculate_lu(matriz, size):
    upper_matriz, lower_matriz = make_matrices(size)
    
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