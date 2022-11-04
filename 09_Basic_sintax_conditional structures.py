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

#Exercício 4
print('\n', '-'*15, 'Exercício 4', '-'*15, '\n')

hidrofobico = ['I', 'V', 'L', 'M', 'C', 'A', 'T', 'F', 'Y', 'W', 'H', 'K']
pequeno = ['P', 'A', 'G', 'C', 'S', 'T', 'D', 'N', 'V']
polar = ['C', 'S', 'T', 'N', 'D', 'Q', 'Y', 'W', 'H', 'K', 'R', 'E']
carregado = ['D', 'E', 'R', 'K', 'H']
aromatico = ['F', 'Y', 'W', 'H']
minusculo = ['A', 'C', 'G', 'S']
alifatico = ['I', 'L', 'V']
hidroxila = ['T', 'S']
acido = ['N', 'Q']
enxofre = ['C', 'M']

aa = input('Aminoácido: ')

print(f'Hidrofóbico: {aa in hidrofobico}')
print(f'Pequeno: {aa in pequeno}')
print(f'Polar: {aa in polar}')
print(f'Carregado: {aa in carregado}')
print(f'Aromático: {aa in aromatico}')
print(f'Minúsculo: {aa in minusculo}')
print(f'Alifático: {aa in alifatico}')
print(f'Hidroxila: {aa in hidroxila}')
print(f'Ácido: {aa in acido}')
print(f'Enxofre: {aa in enxofre}')

#Exercício 5
print('\n', '-'*15, 'Exercício 5', '-'*15, '\n')

newaa = input('Aminoácido: ')

if newaa not in polar:
    print(f'O aminoácido {newaa} é apolar.')
elif newaa not in carregado:
    print(f'O aminoácido {newaa} é neutro.')
else:
    print(f'O aminoácido {newaa} é polar ou carregado.')




# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <