x=float(input("Digite um número:"))
if x <= 0:
    print("X menor ou igual a 0")
elif x <= 100:
    print("X entre 0 e 100")
elif x < 1000:
    print("X entre 100 e 1000")
else:
    print("X maior ou igual a 1000")