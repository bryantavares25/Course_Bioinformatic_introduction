#Atividade 16 - Desafios: Agoritmos de Bioinformatica

#Dasafio 4
print('\n', '-'*15, 'Desafio 4', '-'*15, '\n')

#Distância de Hamming
def dham(seq1, seq2):
    #Distância de Hamming entre duas cadeias de caracteres de mesmo comprimento é o número de posições nas quais elas diferem entre si

    dis = sem = 0

    for let in range(0, len(seq1)):
        if seq1[let] == seq2[let]:
            sem = sem + 1
        else:
            dis = dis+1

    return dis

#def dlev(): #2. A distância de Levenshtein

ss = 'AAAAAAGATTTCACACAACACAG'
aa = 'AAAAAAGTTTTCACACACAACCG'

print(f'Distância de Hamming: {dham(ss, aa)}')


# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <