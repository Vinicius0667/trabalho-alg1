
# -*- coding: utf-8 -*-

#
# Pedro Henrique Urbieta e Vinícius da Silva Mascarenhas
#

def show(matrix, size):
    for i in range(size):
        for n in range(size):
            print(f'{matrix[i][n]:.2f}', end='\t')
        print()
    print()

def showError():
    print('Divisao por zero.')

# Terminar depois
def calculate_lu(matriz, size):
    lower_matriz = matriz
    upper_matriz = make_matrices(size)
    
    for y in range(size):
        for x in range(size):
            if lower_matriz[y][y] != 0 and x > y and x != y:
                multiplier = lower_matriz[y][x] / lower_matriz[y][y]
                
                for i in range(size):
                    lower_matriz[i][x] -= lower_matriz[i][y] * multiplier
                
                upper_matriz[y][x] = multiplier
            elif lower_matriz[y][y] == 0:
                return 0, 0
    
    return upper_matriz, lower_matriz
    
def make_matrices(size: int):
    return [[1 if i == n else 0 for i in range(size)] for n in range(size)]

def main():
    size = int(input())    
    matriz = [list(map(float, input().split())) for _ in range(size)]
    upper_matrix, lower_matrix = calculate_lu(matriz, size)

    if upper_matrix == 0 and lower_matrix == 0:
        showError()
    else: 
        show(lower_matrix, size)
        show(upper_matrix, size)

    return 0
    
main()
