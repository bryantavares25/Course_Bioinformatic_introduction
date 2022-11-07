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



print('Fim')

''' 4. Identifique e imprima a maior dentre as três sequências a seguir.
5. Imprima as três sequências em ordem crescente de tamanho'''




# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <