a = [2,3,4,5,7]
b = a
#COMEÇO
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('\n########################')
b[2]=8 #NÂO ALTERA
print(f'Lista A: {a}')
print(f'Lista B: {b}')
##############NAO MUDOU EX:PONTEIRO
print("#######################")
c = a[:]
c[2]=3 #AGORA ALTERA
print(f'Lista A: {a}')
print(f'Lista C: {c}')
