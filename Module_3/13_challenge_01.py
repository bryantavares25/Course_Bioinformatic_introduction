#Atividade 13 - Desafios: Análise de algoritmos

#Dasafio 1
print('\n', '-'*15, 'Desafio 1', '-'*15, '\n')

def maior(a):
    k = 0

    for i in a:
        if i > k:
            k = i

    return k

inplist = [7, 1, 2, 3, 5]

print(f'A partir da lista: {inplist}. O elemento de maior valor da lista: {maior(inplist)}')

#Dasafio 2
print('\n', '-'*15, 'Desafio 2', '-'*15, '\n')

def mame(b):
    M = 0
    m = 99999

    for l in b:
        if l > M:
            M = l
        if l < m:
            m = l

    return m, M

inplist = [7, 1, 2, 3, 5]

print(f'A partir da lista: {inplist}. O elemento de menor valor e maior valor são, respectivamente: {mame(inplist)}')

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <