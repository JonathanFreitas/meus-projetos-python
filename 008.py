valores = []
valores.append(5)
valores.append(9)
valores.append(90)

print(valores)

for i in valores:
    print(f'{i}...', end='')

print('\n')
for p, i in enumerate(valores):
    print(f'Na posição {p} encontrei 0 {i}')

print('FIM')