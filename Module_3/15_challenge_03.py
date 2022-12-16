#Atividade 14 - Desafios: Análise de algoritmos

#Dasafio 1
print('\n', '-'*15, 'Desafio 1', '-'*15, '\n')

def pesbi(reg, lis):
    
    if len(lis) == 0:
        return -1
    
    esq = 0
    dir = len(lis)-1

    meio = len(lis)//2

    i = int((esq+dir)/2)
    
    while esq<= dir and reg != lis[i]:
        if lis[meio] > reg:
            meio = (lis[meio]//2)+lis[meio]
        else:
            meio = lis[meio]//2
    return (reg, meio)

seqcres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
j = pesbi(2,seqcres)

print(j)

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <