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

#Dasafio 2 e 3
print('\n', '-'*15, 'Desafio 2 e 3', '-'*15, '\n')

def mame(b):
    M = m = b[0]

    for l in b:
        if l < m:
            m = l
        elif l > M:
            M = l

    return m, M

inplist = [7, 1, 2, 3, 5]

print(f'A partir da lista: {inplist}. O elemento de menor valor e maior valor são, respectivamente: {mame(inplist)}')

#Dasafio 4
print('\n', '-'*15, 'Desafio 4', '-'*15, '\n')

def mame4(b):
    
    if (len(b)%2 == 1):
        b.append(b[0])

    if (b[0] < b[1]):
        m = b[0]
        M = b[1]
    else:
        m = b[1]
        M = b[0]

    i = 2
    while (i < len(b)):
        if b[i] > b[i+1]:
            if b[i] > M:
                M = b[1]
            if b[i+1] < m:
                m = b[i+1]
        else:
            if b[i+1] > M:
                M = b[i+1]
            if b[i] < m:
                m = b[i]

        i = i+2

    s = (m, M)
    return s

inplist = [7, 1, 2, 8 , 3, 5, 9]

print(f'A partir da lista: {inplist}. O elemento de menor valor e maior valor são, respectivamente: {mame4(inplist)}.')

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <