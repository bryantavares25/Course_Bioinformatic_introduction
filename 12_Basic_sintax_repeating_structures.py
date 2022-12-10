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
seqlist = ['ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN', 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT', 'ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN']

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
        print(f'{seqlist[i]}\n > > > Sequência de DNA.')
    elif ehRNA:
        print(f'{seqlist[i]}\n > > > Sequência de RNA.')
    else:
        print(f'{seqlist[i]}\n > > > Sequência de Proteína.')
    
    print(erro)

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <