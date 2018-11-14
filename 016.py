def soma(* valores):
    s = 0
    for i in valores:
        s += i
    print(f'Somando os valores {valores} '
          f'temos {s}')

soma(5, 1)
soma(9, 34)