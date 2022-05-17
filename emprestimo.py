casa=int(input("Digite o valor da casa:"))
salario=int(input("Digite o salário:"))
tempo=int(input("Digite a quantidade de meses a pagar:"))
prest=casa/tempo
if prest > salario*30/100:
    print("Empréstimo reprovado!")
else:
    print("Empréstimo aprovado!")