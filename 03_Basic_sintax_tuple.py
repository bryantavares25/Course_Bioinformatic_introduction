#Atividade 3 - Sintaxe básica: Tuples

#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

aa_01 = ('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')

print(aa_01)
print(f'O tamanho da tupla é de {len(aa_01)} elementos')

if 'S' in aa_01: {
    print('Aminoácido serina presente na tupla.')
}
else: {
    print('Aminoácido serina não presente na tupla')
}

aa_02 = ('P', 'G', 'N', 'Y', 'V', 'W')
print(aa_02)

aa_new = aa_01 + aa_02
print(f'Nova tupla: {aa_new}')

print('Quantidade de Glicina: ', aa_new.count('G'))
print('Quantidade de Asparagina: ', aa_new.count('N'))
print('Quantidade de Cisteína: ', aa_new.count('C'))

print('Posição do primeiro elemento de Asparagina: ', aa_new.index('N'))

print('Últimos 5 elementos da tupla: ', aa_new[-5:])
