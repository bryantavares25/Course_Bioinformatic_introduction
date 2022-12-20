#Atividade 16 - Desafios: Agoritmos de Bioinformatica

#Dasafio 4
print('\n', '-'*15, 'Desafio 4', '-'*15, '\n')

# Distância de Hamming
def dham(seq1, seq2):
    #Distância entre duas cadeias de caracteres de mesmo comprimento é o número de posições nas quais elas diferem entre si

    dis = sem = 0

    for let in range(0, len(seq1)):
        if seq1[let] == seq2[let]:
            sem = sem + 1
        else:
            dis = dis+1

    return dis

# Distância de Levenshtein
def dlev(seq1, seq2): #2. A distância de Levenshtein
    #Distância entre duas sequências é o número mínimo de edições dos seguintes tipos que são necessárias para transformar uma sequência na outra (Inserção/Deleção/Substituição)  

    dis = sem = 0

    for let in range(0, len(seq1)):
        if seq1[let] == seq2[let]:
            sem = sem + 1
        elif seq1[seq1+1] == seq2[let]:
            seq1
        else:
            dis = dis+1

    return dis


ss = 'AAAAAAGATTTCACACAACACAG'
aa = 'AAAAAAGTTTTCACACACAACCG'

print(f'Distância de Hamming: {dham(ss, aa)}')


# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <