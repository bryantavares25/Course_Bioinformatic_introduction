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

'''Considere que peptídeos são cadeias formadas por 2 ou mais aminoácidos e não mais que 50
aminoácidos. Dada uma sequência qualquer, verifique se é ou não um peptídeo considerando a definição
de peptídeo aqui apresentada.'''

seq1 = 'ARFGTYUI'



# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <