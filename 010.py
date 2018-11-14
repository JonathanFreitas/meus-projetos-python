teste = list()
teste.append('Jonathan')
teste.append(28)
galera = list()
galera.append(teste[:])#COPIA
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])#COPIA
print(galera)

####################################
print('#########SEM COPIA#########')
teste2 = list()
teste2.append('Josue')
teste2.append(30)
galera2 = list()
galera2.append(teste2)
teste2[0] = 'Fatima'
teste2[1] = 34
galera2.append(teste2)
print(galera2)