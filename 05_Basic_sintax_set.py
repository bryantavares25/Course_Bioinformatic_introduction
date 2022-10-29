#Atividade 5 - Sintaxe básica: Sets

#Exercício 1
print('\n', '-'*15, 'Exercício 1', '-'*15, '\n')

f1 = {1.9, 1.8, 5.7, 1.6, 5.8, 1.7, 9.6, 5.9, 9.5, 6.5, 6.2, 1.1, 4.4, 3.5, 2.9, 4.7,4.6, 5.2, 5.3}
f2 = {4.7, 3.6, 6.2, 7.1, 7, 5.6, 5.7, 3.4, 3.3, 2.1, 3.8, 3.9, 5, 5.1, 1.9, 9.5, 1.0, 1.3, 5.4}
f3 = {2.2, 3.3, 5.1, 3, 3.7, 9.1, 8.8, 8.5, 2, 4.1, 6.1, 4.9, 1.1, 0.5, 0.8, 3.2, 6.9, 9.3, 9.5}

fd12 = f1.difference(f2)
print(f'\nDiferença entre a ferramenta 1 e 2: {fd12}')
fi12 = f1.intersection(f2)
print(f'Intersecção entre a ferramenta 1 e 2: {fi12}')

fd13 = f1.difference(f3)
print(f'\nDiferença entre a ferramenta 1 e 3: {fd13}')
fi13 = f1.intersection(f3)
print(f'Intersecção entre a ferramenta 1 e 2: {fi13}')

fd23 = f2.difference(f3)
print(f'\nDiferença entre a ferramenta 2 e 3: {fd23}')
fi23 = f2.intersection(f3)
print(f'Intersecção entre a ferramenta 1 e 2: {fi23}')

f1.update(f2, f3)
print(f'\nNovo conjunto com os valores de todos os grupos: {f1} \nTamanho do novo conjunto: {len(f1)}.')

#Exercício 2
print('\n', '-'*15, 'Exercício 2', '-'*15, '\n')

a = {3, 6, 9, 12, 15, 18, 21, 24, 28, 27}
b = {2, 6, 8, 10, 14, 16, 18, 20, 22, 24}
c = {2, 6, 10, 18, 20}
d = {1, 30, 5, 11, 17, 16, 22, 26}

iab = a.intersection(b)
dab = a.difference(b)

print(f'\nInersecção entre A e B: {iab}.\n Diferença entre A e B: {dab}')

quest_ad = a.isdisjoint(d)
print(f'\nO conjunto A é disjunto do conjunto D? {quest_ad}')

quest_bd = b.isdisjoint(d)
print(f'\nO conjunto B é disjunto do conjunto D? {quest_bd}')

quest_ca = c.issubset(a)
print(f'\nO conjunto C é um subconjunto de A? {quest_ca}')

quest_cb = c.issubset(b)
print(f'\nO conjunto C é um subconjunto de B? {quest_cb}')

d.update([18, 23, 25, 63])
print(f'\nConjunto D com adições de novos items ([18, 23, 25, 63]): {d}')
