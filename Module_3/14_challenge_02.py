#Atividade 14 - Desafios: Análise de algoritmos

#Dasafio 1
print('\n', '-'*15, 'Desafio 1', '-'*15, '\n')

trm = ['ABC', 'ABD', 'ABE', 'ABF']

def sear(reg, lis):
    for i in range(0, len(lis)):
        if lis[i] == reg:
            return(i)
    return -1

out = sear('ABE', trm)
print(out)

def pqord(reg, lis):
    i = 0
    while i < len(lis) and reg >= lis[i]:
        if lis[i] == reg:
            return i
        i=i+1
    return -1

seqcres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

ord = pqord(7, seqcres)
print(ord)

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <