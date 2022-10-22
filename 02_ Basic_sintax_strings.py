#Atividade 02 - Sintaxe Básica

#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

tnf_seq = 'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'

print(f'Tamanho da sequência: {len(tnf_seq)} aminoácidos.')
print(f'Quantidade de LL na sequência: {tnf_seq.count("LL")}.')
print(f'Posição de GG na sequência: {tnf_seq.find("GG")}.')
print(f'Posição de RR na sequência: {tnf_seq.find("LL")}')
print(f'Amostra dos 100 primeiros aminoácidos: {tnf_seq[:100]}')
tnf_subs = tnf_seq.replace('SSSR', 'AAAA')
print(f'Substituição de SSSR para AAAA: {tnf_subs}.')
tnf_cleave = tnf_subs.split('AAAA')
print(f'{tnf_cleave}')

#Exercício 2
print('\n', '-'*15, 'Exercício 2', '-'*15, '\n')

texto = 'As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos. Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do se nome.'

print(f'Texto em letras maiúsculas: {texto.upper()} \n')
print(f'Texto para letras minúsculas: {texto.lower()} \n')
print(f'Texto misto entre letras minúsculas e maiúsculas: {texto.title()} \n')
print(f'Texto misto entre letras minúsculas e maiúsculas: {texto.title().swapcase()} \n')

#Exercício 3
print('\n', '-'*15, 'Exercício 3', '-'*15, '\n')

insulin_signal = 'MALWMRLLPLLALLALWGPDPAAA'

print(f'Tamanho da sequência da insulina: {len(insulin_signal)}.')
insulin_signal_cleavage = insulin_signal.split('LLALLALWG')
insulin_new = insulin_signal_cleavage[0] + insulin_signal_cleavage[1]
print(f'Sequência clivada: {insulin_new}')
print(f'Substituição de sequência: {insulin_new.replace("DPAAA", "LLALL")}')

#Exercício 4
print('\n', '-'*15, 'Exercício 4', '-'*15, '\n')

DNA_seq = 'GATGGAACTTGACGTAAACCTATATT'
RNA_seq = DNA_seq.replace('T', 'U')

print(f'Sequência de DNA: {DNA_seq}.\nSequência de RNA: {RNA_seq}')
