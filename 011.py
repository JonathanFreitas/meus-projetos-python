pessoas = [['joao', 19], ['Ana', 33], ['joaquim', 13], ['Maria', 45]]
print(pessoas)
print(pessoas[1:])#Ana ate o final
print(pessoas[2][1])#so a idade de joaquim
print(pessoas[1])#So Ana

#################EXEMPLO#################
print("#########################")
totamai = totamen =0
galera = list()
dado = list()
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])#IMPORTANTE
    dado.clear()

print(galera)

for o in galera:
    if o[1] >=21:
        print(f'{o[0]} e maior de idade')
        totamai += 1
    else:
        print(f'{o[0]} e menor de idade')
        totamen += 1

print(f'Temos {totamai} maiores e {totamen} menores de idade')

