#Atividade 17 - Desafios: Agoritmos de Bioinformatica

#Dasafio 6
print('\n', '-'*15, 'Desafio 6', '-'*15, '\n')

def lcs(v, w):
    pontuacao = []
    ponteiros = []

    pontuacao = [0]*len(v)
    ponteiros = ['']*len(v)

    # Inicialiazação de duas matrizes vazias
    for i in range(0,len(w)):
        pontuacao[i] = [0]*len(v)
        ponteiros[i] = ['']*len(v)

    # i para linhas, j para colunas
    for i in range(0,len(w)):
        ponteiros[i][0] = '|'
    for j in range(0, len(v)):
        ponteiros[0][i] = '_'

    for i in range(1,len(w)):
        for j in range(1, len(v)):
            pontuacao[i][j] = max(v[j], w[i], pontuacao[i-1][j], pontuacao[i][j-1], pontuacao[i-1][j-1])
            ponteiros[i][j] = pon(v[j], w[i], pontuacao[i-1][j], pontuacao[i][j-1], pontuacao[i-1][j-1])

    impmatriz(v, w, pontuacao, ponteiros)
    alinhafin(v, w, pontuacao, ponteiros)

# Pensando modificações para levar em conta matrizes de substituição
def max(s1, s2, c, l, d, mat, mis, indel):
    if (s1 == s2 and (d+mat) >= c and d+mat >= l):
        d = d+mat
        return d
    elif (s1 != s2 and (d+mis) >= c and d+mis >= l):
        d = d+mis
        return d
    elif (l >= c and l >= d):
        return l-indel
    else:
        return c

def pon(s1, s2, c, l, d):
    if (s1 == s2 and (d+1) >= c and d+1 >= l):
        return '\\'
    elif (l >= c and l >= d):
        return '_'
    else:
        return '|'

def impmatriz(v, w, pontuacao, ponteiros):

    print('\t', end='')
    for j in range(0, len(v)):
        print(v[j], end='\t')
    
    print()
    for i in range(0, len(w)):
        print(w[i], end='\t')
        for j in range(0, len(v)):
            print(pontuacao[i][j], ponteiros[i][j], end='\t', sep='')
        print()
    print()

def alinhafin(v, w, pontuacao, ponteiros):
    v_alinha = ''
    w_alinha = ''

    i = len(w)-1
    j = len(v)-1

    while ((i!=0) or (j!=0)):
        if (ponteiros[i][j] == '\\'):
            v_alinha = v[j]+ v_alinha
            w_alinha = w[i]+ w_alinha
            i = i-1
            j = j-1
        elif (ponteiros[i][j]=='_'):
            v_alinha = v[j]+v_alinha
            w_alinha = '_'+w_alinha
            j = j-1
        else:
            v_alinha = '_'+ v_alinha    
            w_alinha = w[i]+ w_alinha
            i = i-1

    print(pontuacao[len(w)-1][len(v)-1])
    print(v_alinha)
    print(w_alinha)

seq1 = ['*','A', 'A', 'C', 'G', 'T', 'T', 'A', 'T', 'G']
seq2 = ['*', 'A', 'C', 'C', 'G', 'T', 'T', 'G', 'T', 'G']

lcs(seq1, seq2)

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <