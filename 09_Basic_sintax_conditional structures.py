#Atividade 8 - Sintaxe básica: Operadores

#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

bioseq = 'AAAAAAAAAAAATATATATATATATTATATAGCA'
lenbioseq = len(bioseq)

if lenbioseq >= 50:
    print(f'{bioseq}\n\n > Sequência apta para análise, pois tem mais de {lenbioseq} nucleotídeos.')
else:
    print(f'{bioseq}\n\n > Sequência inapta para análise, pois tem menos de {lenbioseq} nucleotídeos')

#Exercício 2
print('\n', '-'*15, 'Exercício 2', '-'*15, '\n')

seq1 = 'ARFGTYUI'

if len(seq1) <= 50 and len(seq1) >=2:
    print(f'{seq1}\n\n > A sequência é um peptídeo')
else:
    print(f'{seq1}\n\n > A sequência não é um peptídeo')

#Exercício 3
print('\n', '-'*15, 'Exercício 3', '-'*15, '\n')

'''Considere agora que peptídeos podem ser divididos em:
• 2 aminoácidos: Dipeptídeo
• 3 aminoácidos: Tripeptídeo
• 4 ou mais aminoácidos (com até 50 aminoácidos): Polipeptídeo
Imprima se é um peptídeo e a denominação adequada.'''

seq2 = 'WWWMNBVCXZHJKKLASLIUYTREWQERTYUIOPASDFGHJKKLASL'
lenseq2 = len(seq2)

if lenseq2 <= 50 and lenseq2 >= 2:
    print(f'{seq2}\n\n> Sequência é um peptídeo:', end='')
    if lenseq2 == 2:
        print(' Dipeptídeo.')
    elif lenseq2 == 3:
        print(' Tripeptídeo.')
    else:
        print(' Polipeptídeo.')
else:
    print(f'{seq2}\n\n > Sequência não é um peptídeo.')

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <