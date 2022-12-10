#Atividade 11 - Sintaxe básica: Estruturas de repetição

#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

for i in range(0,11):
    print(i, end=' ')

print('')

num = 0

while num < 11:
    print(num, end=' ')
    num = num + 1

print('')

#Exercício 2
print('\n', '-'*15, 'Exercício 2', '-'*15, '\n')

for l in range(0,11,2):
    print(l, end=' ')

print('')

mun = 0

while mun < 11:
    if mun%2==0:
        print(mun, end=' ')
    else:
        print('', end='')
    
    mun = mun + 1

print('')

#Exercício 3
print('\n', '-'*15, 'Exercício 3', '-'*15, '\n')

sedna = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'

for i in sedna:
    if i == 'A' or i == 'T' or i == 'C' or i == 'G':
        print('DNA', end=' ')
    else:
        print('Não DNA')

print('')

#Exercício 4
print('\n', '-'*15, 'Exercício 4', '-'*15, '\n')

for q in range(1,101):
    print(f'Número {q}. Divisores:', end= ' ')
    for w in range(1,q+1):
        if q%w==0:
            print(f'{w}', end=' ')
        else:
            print('', end='')
    print('')

#Exercício 5
print('\n', '-'*15, 'Exercício 5', '-'*15, '\n')

print('Números primos: ')

for q in range(1,1001):
    qlist = []
    for w in range(1,q+1):
        if q%w==0:
            qlist.append(w)
        else:
            print('', end='')

    if len(qlist) == 2:
        print(f' <<< {q} >>> {qlist}')
    else:
        print('', end= '')

#Exercício 6
print('\n', '-'*15, 'Exercício 6', '-'*15, '\n')

seqref = 'VRSSSRTPSDKPVAAAAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLAAAFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKAAASPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAAAAEINRPDYLLFAESGQVYFGIIAL'

for i in range(0, len(seqref)):
    if seqref[i:i+3] == 'AAA':
        print('AAA em', i)

#Exercício 7
print('\n', '-'*15, 'Exercício 7', '-'*15, '\n')

micseq = ['KTCENLA', 'DTFR', 'GPCFTDGSC', 'DDHCKNKEHLIK', 'GRCRDDFRC', 'WCTRNC', 'ATC']

print(f'Sequências: {micseq}. Dentre estas a maior é: {max(micseq)}')

maiortam = 0
maiorind = 0

for i in range(0, len(micseq)):
    if len(micseq[i]) > maiortam:
        maiortam = len(micseq[i])
        maiorind = i

print(micseq[maiorind], maiortam)

#Exercício 8
print('\n', '-'*15, 'Exercício 8', '-'*15, '\n')

numlist = [1,4,6,3,4,5,7,8,9,5,6,7,4,3,5,6,7,8]

soma = 0

for i in range(0,len(numlist)):
    soma = soma + i

print(f'A média dos termos {numlist} é {soma/len(numlist)}')

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <