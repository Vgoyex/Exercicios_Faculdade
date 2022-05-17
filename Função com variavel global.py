a = 5
def muda_e_imprime():
    global a
    a = 7
    print(f'a dentro da função:{a}')
print(f'a antes de mudar:{a}')
muda_e_imprime()
print(f'a depois de mudar:{a}')

''' Execução:
a antes de mudar:5
a dentro da função:7
a depois de mudar:5'''