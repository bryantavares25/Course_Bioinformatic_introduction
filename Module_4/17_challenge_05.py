#Atividade 17 - Desafios: Agoritmos de Bioinformatica

#Dasafio 5
print('\n', '-'*15, 'Desafio 5', '-'*15, '\n')


def lcs(v, w):
    pontuacao = []
    ponteiros = []

    pontuacao = [0]*len(v)
    ponteiros = ['']*len(v)

    for i in range(0,len(w)):
        pontuacao[i] = [0]*len(v)
        ponteiros[i] = ['']*len(v)

    for i in range(0,len(w)):
        ponteiros[i][0] = '|'
    
    for i in range(0, len(v)):
        ponteiros[0][i] = '_'

seq1 = ['*','A', 'A', 'C', 'G', 'T', 'T', 'A', 'T', 'G']
seq2 = ['*', 'A', 'C', 'C', 'G', 'T', 'T', 'G', 'T', 'G']

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <