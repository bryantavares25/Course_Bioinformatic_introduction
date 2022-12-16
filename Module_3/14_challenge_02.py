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

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <