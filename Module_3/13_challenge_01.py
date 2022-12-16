#Atividade 12 - Sintaxe básica: Estruturas de repetição

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
    
    print(f'O elemento de maior valor da lista: {k}.')

inplist = [7, 1, 2, 3, 5]

print(f'A partir da lista: {inplist}.', end='')
maior(inplist)

# B. A. R. T. > < ( ( (º > Rm 11:36 < º ) ) ) > <