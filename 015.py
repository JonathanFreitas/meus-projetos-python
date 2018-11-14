#Funçoes
def mostraLinha():
    print('-' * 30)
def inicioTela():
    mostraLinha()
    print('    SISTEMA DE ALUNOS    ')
    mostraLinha()
    mostraLinha()
    print('   CADASTRO DE FUNC    ')
    mostraLinha()
    mostraLinha()
    print('   ERRO SISTEMA      ')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] += 2
        pos += 1

valores = [6, 2, 3, 4, 7, 9]
dobra(valores)
print(valores)