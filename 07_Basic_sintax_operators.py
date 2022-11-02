#Atividade 7 - Sintaxe básica: Operadores

#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

a = 10
b = 11

print(f'O número {a} é igual ao número {b}: {a==b}')

#Exercício 2
print('\n', '-'*15, 'Exercício 2', '-'*15, '\n')

a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5

am = (a1+a2+a3+a4+a5)/5

print(f'A média entre os números {a1}, {a2}, {a3}, {a4} e {a5}: {am}')

#Exercício 3
print('\n', '-'*15, 'Exercício 3', '-'*15, '\n')

b = 5
e = 2

print(f'Valor da base {b} elevada pelo expoente {e} é {b**e}')

#Exercício 4
print('\n', '-'*15, 'Exercício 4', '-'*15, '\n')

n1 = 1001
n2 = 2

nt = 0 == n1%n2

print(f'O número {n1} é divisível por {n2}: {nt}')

#Exercício 5
print('\n', '-'*15, 'Exercício 5', '-'*15, '\n')

print(f'O quociente inteiro da divisão de {n1} por {n2}: {n1//n2}')

#Exercício 6
print('\n', '-'*15, 'Exercício 6', '-'*15, '\n')

seqbio = 5
seqbiover = seqbio <= 5 or seqbio >= 30

print(f'A sequência tem tamanho entre 5 e 30: {seqbiover}')

#Exercício 8
print('\n', '-'*15, 'Exercício 8', '-'*15, '\n')

aalist = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
letter = 'Z'

print(f'O aminoácido {letter} está presente na lista {aalist}: {letter in aalist}')

#Exercício 9
print('\n', '-'*15, 'Exercício 9', '-'*15, '\n')

pos = ['H', 'K', 'R']
neg =['D', 'E']

a = 'H'

if a in pos:
    print('O aminoácido é carregado positivamente.')
elif a in neg:
    print('O aminoácido é carregado negativamente.')
else:
    print('O aminoácido não é carregado.')

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <