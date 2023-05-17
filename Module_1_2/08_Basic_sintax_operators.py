#Atividade 8 - Sintaxe básica: Operadores

import math

#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

# Resíduos de glicina

g1 = [[108.304, 100.827, 67.992], [108.477, 100.389, 69.362], [109.907, 100.555, 69.817], [110.821, 100.799, 69.027]]
g2 = [[107.670, 101.359, 70.074], [108.477, 100.389, 69.362], [109.513, 101.011, 68.450], [110.667, 100.572, 68.425]]

print(f'Glicina 1: {g1}\n')
print(f'Glicina 2: {g2}\n')

#RMSD (Root Mean Square Deviation)

# 1º Soma para cada um dos átomos
temN = (g1[0][0] - g2[0][0])**2 + (g1[0][1] - g2[0][1])**2 + (g1[0][2] - g2[0][2])**2
temCA = (g1[1][0] - g2[1][0])**2 + (g1[1][1] - g2[1][1])**2 + (g1[1][2] - g2[1][2])**2
temCB = (g1[2][0] - g2[2][0])**2 + (g1[2][1] - g2[2][1])**2 + (g1[2][2] - g2[2][2])**2
temO = (g1[3][0] - g2[3][0])**2 + (g1[3][1] - g2[3][1])**2 + (g1[3][2] - g2[3][2])**2

# 2º Soma de todos os átomos
soma = temN + temCA + temCB + temO

# 3º Divisão da soma pela quantidade de átomos pareados
quoc = soma/len(g1)

# 4º Raíz quadrada da divisão
raiz = math.sqrt(quoc)

# Valor final de RMSD
print(f'O RMSD entre os dois resíduos de glicina é: {raiz}')

#Exercício 2
print('\n', '-'*15, 'Exercício 2', '-'*15, '\n')

#Sequências
seqa = 'ATGATCTCGTAATTAACCGGAATTTTGGGCC'
seqb = 'GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA'

#Guanina/Citosina
gca = ((seqa.count('G') + seqa.count('C')) * 100) / len(seqa)
gcb = ((seqb.count('G') + seqb.count('C')) * 100) / len(seqb)

#Imprimindo
print(f'Sequência A: {seqa} \n {gca}% de conteúdo GC. \n')
print(f'Sequência B: {seqb} \n {gcb}% de conteúdo GC. \n')

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <