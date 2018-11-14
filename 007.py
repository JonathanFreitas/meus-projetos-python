num = [77,2,22,34,5,6,11]
print(num)
num[0] = 0 #Inserir o 0
print(num[0])
print(num)
num.append(7)
print(num)
num.sort(reverse=True)
print(num)
print(f'Esta lista tem {len(num)} elementos')
num.insert(2,0) #irar inserir o 0
print(num)
num.pop(2) #Elimina o 0
print(num)
num.remove(22)
print(num)
