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

med = ((SeqA+SeqB+SeqC)/3)

for n in lseq:
    if len(n) >= med:
        print(f'Sequência é maior que o tamanho médio das sequências:\n> {n}\n')
    else:
        print('Sequência é menor que o tamanho médio das sequências.\n')

print('Fim')

'''Imprima apenas as sequências com 80 ou mais aminoácidos.
2. Imprima apenas as sequências cujo tamanho seja maior que a média de tamanho das sequências.
3. Imprima apenas as sequências que possuam pelo menos uma histidina (H) e nenhuma prolina (P).
4. Identifique e imprima a maior dentre as três sequências a seguir.
5. Imprima as três sequências em ordem crescente de tamanho'''




# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <