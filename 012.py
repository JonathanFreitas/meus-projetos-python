pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} '
      f'tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
###############################
print('#########################')
pessoas['nome'] = 'Jonathan'
for k in pessoas.keys():
    print(k, end=' ')
for p in pessoas.values():
    print(p, end=' ')
#del pessoas['sexo'] #APAGA SEXO

print('----Fim----')