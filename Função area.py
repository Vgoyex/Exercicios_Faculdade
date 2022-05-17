def main():
    numeroDigitado = int(input("Digite um número inteiro e positivo: "))
    while numeroDigitado > 0:
        #Cálculo do Fatorial e armazenamento na variável fatorial
        fatorial = calculaFatorial (numeroDigitado)
        print('O fatorial de ', numeroDigitado, 'é', fatorial)
        numeroDigitado = int(input("Digite um número inteiro e positivo: "))

def calculaFatorial(n):
    cont = 1
    fat = 1
    while cont <= n:
        fat = fat * cont
        cont += 1
    return fat
