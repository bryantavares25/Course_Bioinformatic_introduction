#Atividade 17 - Desafios: Agoritmos de Bioinformatica

#Dasafio 5
print('\n', '-'*15, 'Desafio 5', '-'*15, '\n')


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

    impmatriz =
    alinhafin =

def max(s1, s2, c, l, d):
    if (s1 == s2 and (d+1) >= c and d+1 >= l):
        d = d+1
        return d
    elif (l >= c and l >= d):
        return l
    else:
        return c

def pon(s1, s2, c, l, d):
    if (s1 == s2 and (d+1) >= c and d+1 >= l):
        return '\.'
    elif (l >= c and l >= d):
        return '_'
    else:
        return '|'

def impmatriz(v, w, pontuacao, ponteiros):

    print('t', end='')
    for j in range(0, len(v)):
        print(v[j], end='t')
    
    print()
    for i in range(0, len(w)):
        print(w[i], end='t')
        for j in range(0, len(v)):
            print(pontuacao[i][j], ponteiros[i][j], end='t', sep='')
        print()
    print()


seq1 = ['*','A', 'A', 'C', 'G', 'T', 'T', 'A', 'T', 'G']
seq2 = ['*', 'A', 'C', 'C', 'G', 'T', 'T', 'G', 'T', 'G']



# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <