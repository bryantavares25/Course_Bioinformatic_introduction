#Atividade 3 - Sintaxe básica: Tuples

#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

ncbi_id = ['AAY66821.1', 'AAY66759.1', 'AAY66711.1', 'AAY66706.1', 'AAY66703.1', 'AAY66697.1', 'AAY66696.1', 'AAY66682.1', 'AAY66647.1', 'AAY66625.1', 'AAY66623.1', 'AAY66620.1', 'AAY66619.1', 'AAY66616.1', 'AAY66609.1', 'AAY66607.1', 'AAY66586.1', 'AAY66564.1', 'AAY66562.1', 'AAY66561.1', 'AAY66558.1', 'AAY66544.1', 'AAY66542.1', 'AAY66539.1', 'AAY66538.1', 'AAY66537.1', 'AAY66536.1', 'AAY66512.1', 'AAY66496.1', 'AAM93627.1', 'AAM93626.1', 'AAY66506.1', 'AAM93587.1', 'AAY66811.1', 'AAY66620.1', 'AAY66555.1', 'AAY66707.1', 'AAM93653.1', 'AAY66608.1', 'AAY66700.1', 'AAY66646.1', 'AAY66809.1', 'AAK97814.1', 'AAK97810.1', 'AAY66594.1', 'AAY66685.1', 'AAY66571.1', 'AAY66865.1']
l_ni = len(ncbi_id) 

print(f'\nLista NCBI: {ncbi_id}')
print(f'\nO tamanho da lista inicial: {l_ni}')

pot_ncbi_id = ['AAY66682.1', 'AAY66504.1', 'AAY66640.1', 'AAY66562.1', 'AAY66816.1']

print(f'\nVerificando a presença dos IDs ({pot_ncbi_id}) na lista do NCBI:')
for i in pot_ncbi_id:
    print(f'{i}: {i in pot_ncbi_id} - Quantidade: {ncbi_id.count(i)}')

print(f'\nElemento na posição 10 da lista: {ncbi_id[10]}')

print(f'Inserindo o itens AAY66967.1 na lista do NCBI... Carregando...')
ncbi_id.insert(11, 'AAY66967.1')

print(f'Inserindo o itens AAY66967.1 na lista do NCBI... Carregando...')
ncbi_id.insert(21, 'AAY66880.1')

print(f'Inserindo o itens AAY66967.1 na lista do NCBI... Carregando...')
ncbi_id.insert(16, 'AAY66874.1')

print(ncbi_id[11])
