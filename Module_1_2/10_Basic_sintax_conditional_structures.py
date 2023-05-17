#Atividade 10 - Sintaxe básica: Estruturas condicionais

SeqA = 'LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK'
SeqB = 'KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS'
SeqC = 'CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR'

lseq = [SeqA, SeqB, SeqC]

#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

for n in lseq:
    if len(n) >= 80:
        print(f'Sequência com oitenta ou maus aminoácidos:\n> {n}\n')
    else:
        print('Sequência com menos de oitenta aminoácidos.\n')

#Exercício 2
print('\n', '-'*15, 'Exercício 2', '-'*15, '\n')

med = ((len(SeqA)+len(SeqB)+len(SeqC))/3)

for n in lseq:
    if len(n) >= med:
        print(f'Sequência é maior que o tamanho médio das sequências:\n> {n}\n')
    else:
        print('Sequência é menor que o tamanho médio das sequências.\n')

#Exercício 3
print('\n', '-'*15, 'Exercício 3', '-'*15, '\n')

for n in lseq:
    if 'H' in n and 'P' not in n:
        print(f'Sequência com Histidina e sem Prolina:\n> {n}\n')
    else:
        print('Sequência sem Histidina e/ou com Prolina.\n')

#Exercício 4
print('\n', '-'*15, 'Exercício 4', '-'*15, '\n')

if len(SeqA)>len(SeqB) and len(SeqA)>len(SeqB):
    print('SeqA é a maior sequência.')
elif len(SeqB)>len(SeqA) and len(SeqB)>len(SeqC):
    print('SeqB é a maior sequência.')
else:
    print('SeqC é a maior sequência.')

#Exercício 5
print('\n', '-'*15, 'Exercício 5', '-'*15, '\n')

if len(SeqA)>len(SeqB) and len(SeqA)>len(SeqC):
    print('SeqA')
    if len(SeqB)>(SeqC):
        print('SeqB')
        print('SeqC')
    else:
        print('SeqC')
        print('SeqB')
elif len(SeqB)>len(SeqA) and len(SeqB)>len(SeqC):
    print('SeqB')
    if len(SeqA)>(SeqC):
        print('SeqA')
        print('SeqC')
    else:
        print('SeqC')
        print('SeqA')
elif len(SeqC)>len(SeqA) and len(SeqC)>len(SeqB):
    print('SeqC')
    if len(SeqC)>(SeqB):
        print('SeqC')
        print('SeqB')
    else:
        print('SeqB')
        print('SeqC')
else:
    print('Deu ruim chapa.')
    
# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <