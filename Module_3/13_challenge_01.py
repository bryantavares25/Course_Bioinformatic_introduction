#Atividade 12 - Sintaxe básica: Estruturas de repetição

# Projete um algoritmo e implemente uma função em Python que receba como entrada uma lista e retorne o maior elemento desse conjunto.
# Descubra quais as operações mais relevantes em termos de tempo de execução de seu programa.
# Tente calcular a função de complexidade de tempo f(n) de seu programa.
# Você acha que seu programa é ótimo?


#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

def maior(a):
    k = 0

    for i in a:
        if i > k:
            k = i
    
    print(f'{k} é o maior valor da lista')

inplist = [7, 1, 2, 3, 5]

print(f'A partir da lista: {inplist}.\nResultado: ', end='')
maior(inplist)

# Estrutura funcional de uma classe
#class Proteína:
#    def __init__(self, nome, tamanho):
#        self.nome = nome
#        self.tamanho = tamanho
#    
#    def minhafuncao(self):
#        print('Proteína: ' + self.nome)
#
#p1 = Proteína('Horácio', 237)
#
#p1.minhafuncao()

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <