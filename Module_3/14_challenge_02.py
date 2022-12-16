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

#Desafio
#1. Esse algoritmo é ótimo?
#2. Se não, como ele poderia ser melhorado?
#3. Tente implementar melhorias e demonstrar através da nova função de complexidade
#que ele é mais eficiente



# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <