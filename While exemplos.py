contador = 1
resposta = 'sim'
while (resposta == 'sim' or resposta == 's'):
    x = int(input("Digite um valor x: "))
    r = x*3
    print ("O valor de R é: ",r)
    resposta = input("Deseja continuar ?")
else:
    print("Obrigado!")