acerto = 0
resposta=str(input("Escreva resposta da primeira questão: : a, b, c, d ou e: "))
resposta2=str(input("Escreva resposta da segunda questão: a, b, c, d ou e: "))
resposta3=str(input("Escreva resposta da terceira questão: : a, b, c, d ou e: "))
if resposta == "b" or resposta=="B":
    acerto = acerto+1
if resposta2 == "a" or resposta2=="A":
    acerto = acerto+1
if resposta3 == "d" or resposta3=="D":
    acerto = acerto+1
    print("Total de acertos: ",acerto)
else:
    print("Total de acertos: 0")