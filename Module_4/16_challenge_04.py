#Atividade 16 - Desafios: Agoritmos de Bioinformatica

#Dasafio 4
print('\n', '-'*15, 'Desafio 4', '-'*15, '\n')

#Distância de Hamming
def dham(seq1, seq2):

    dis = sem = 0

    #Contar as modificações necessárias para que as sequências se tornem identicas
    for let in range(0, len(seq1)):
        if seq1[let] == seq2[let]:
            sem = sem + 1
        else:
            dis = dis+1

    return dis

#def dlev(): #2. A distância de Levenshtein

ss = 'AAC'
aa = 'AAB'

print(f'Distância de Hamming: {dham}')


# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <