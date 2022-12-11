#Atividade 12 - Sintaxe básica: Estruturas de repetição

#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

for fah in range (1,151):
    print(f'    {fah}° F    {(5*(fah-32))/9:.2f}° C')

#Exercício 2
print('\n', '-'*15, 'Exercício 2', '-'*15, '\n')

#Sets
DNA = {'A', 'G', 'T', 'C'}
RNA = {'U', 'C', 'A', 'G'}
PROTEINA = {'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'} 

#Lista com sequências
seqlist = ['ZZXMLXZZ', 'ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN', 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT', 'ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN']

# Estrutura de repetição para cada item da lista
for i in range(0,len(seqlist)):
    erro = []

    # Estrutura de repetição para cada item do texto
    for o in seqlist[i]:
        
        # Teste DNA
        ehDNA = True
        
        if (not o in DNA):
            ehDNA = False
            erro.append(o)
        
        # Teste RNA
        ehRNA = True

        if (not o in RNA):
            ehRNA = False
            erro.append(o)

        # Teste Proteína
        ehProteina = True

        if (not o in PROTEINA):
            ehProteina = False
            erro.append(o)

    if ehDNA:
        print(f'{seqlist[i]} > > > Sequência de DNA.\n')
    elif ehRNA:
        print(f'{seqlist[i]} > > > Sequência de RNA.\n')
    elif ehProteina:
        print(f'{seqlist[i]} > > > Sequência de Proteína.\n')
    else:
        errouni = set(erro)
        print(f'{seqlist[i]} > > > Não é nenhum tipo de molécula biológica. ERRO: {errouni}.\n')

#Exercício 3
print('\n', '-'*15, 'Exercício 3', '-'*15, '\n')

dnaseq =   'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'

dnalist = list(dnaseq)
dnalist.reverse()

dnacom = []
dnastr = ''

for p in range(0, len(dnalist)):
    if dnalist[p] == 'A':
        dnacom.append('T')
    elif dnalist[p] == 'T':
        dnacom.append('A')
    elif dnalist[p] == 'C':
        dnacom.append('G')
    elif dnalist[p] == 'G': 
        dnacom.append('C')

for a in dnacom:
    dnastr = dnastr+a

print(dnaseq)
print(dnastr)

#Exercício 4
print('\n', '-'*15, 'Exercício 4', '-'*15, '\n')

# Escreva um programa que calcule o fatorial de um número recebido como entrada.
#numfat = int(input('Número de entrada: '))
numfat = 5
fat = 1

for n in range(1,numfat+1):
    fat = fat*n
    print(fat, end = ' ')

print(f'\nO valor do fatorial de {numfat} é {fat}.')

#Exercício 5
print('\n', '-'*15, 'Exercício 5', '-'*15, '\n')

print('TABUADAS')

for z in range(1,16):   
    print(f'- - Tabuada do número {z} - -')
    for x in range(1,11):
        print(f'> {z} X {x} = {z*x}')

#Exercício 6
print('\n', '-'*15, 'Exercício 6', '-'*15, '\n')

prot = 'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'

aamass = {'A':71.03711, 'C':103.00919, 'D':115.02694, 'E':129.04259, 'F':147.06841, 'G':57.02146, 'H':137.05891, 'I':113.08406, 'K':128.09496, 'L':113.08406, 'M':131.04049, 'N':114.04293, 'P':97.05276, 'Q':128.05858, 'R':156.10111, 'S':87.03203, 'T':101.04768, 'V':99.06841, 'W':186.07931, 'Y':163.06333}

massamolar = 0

for v in prot:
    massamolar = massamolar+aamass[v]
    
print(f'A proteína {prot} de tamanho {len(prot)} tem massa molar de {massamolar}.')

#Exercício 7
print('\n', '-'*15, 'Exercício 7', '-'*15, '\n')

# A) a menor sequência e seu comprimento
# B) a maior sequência e seu comprimento
# C) a média entre os comprimentos das sequências
# D) a mediana entre os comprimentos das sequências

ref = ['Entry ID', 'Entity ID', 'Chain ID', 'Database Name', 'Accession Code(s)', 'Sequence', 'Chain Length', 'Entity Macromolecule Type', 'Molecular Weight (Entity)']
table = [['3PSM', 1 , 'A,B', 'UniProt', 'Q6B519', 'KTCENLADTFRGPCFTDGSCDDHCKNKEHLIKGRCRDDFRCWCTRNC', 47, 'polypeptide(L)', 5.511], ['2NY9', 1 , 'X', 'UniProt', 'Q17027', 'ATCDLASGFGVGSSLCAAHCLVKGYRGGYCKNKICHCRDKF', 41, 'polypeptide(L)', 4.349], ['2NY8', 1 , 'X', 'UniProt', 'Q17027', 'ATCDLASGFGVGSSLCAAHCIARRYRGGYCNSKAVCVCRN', 40, 'polypeptide(L)', 4.148], ['2NZ3', 1 , 'A', 'UniProt', 'Q17027', 'ATCDLASIFNVNHALCAAHCIARRYRGGYCNSKAVCVCRN', 40, 'polypeptide(L)', 4.353], ['2E3G', 1 , 'A', 'UniProt', 'Q17027', 'ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN', 40, 'polypeptide(L)', 4.525], ['2E3F', 1 , 'A', 'UniProt', 'Q17027', 'ATCDLASFSSQWVTPNDSLCAAHCIARRYRGGYCNGKRVCVCR', 43, 'polypeptide(L)', 4.747], ['2E3E', 1 , 'A', 'UniProt', 'Q17027', 'ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF', 45, 'polypeptide(L)', 5.007]]


print(table[0][8])



# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <