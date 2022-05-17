def maxi (a,b):
    if a > b:
        return(a)
    else:
        return(b)
x = int(input("Digite o 1° número: "))
y = int(input("Digite o 2° número: "))
result = maxi(x,y)
print('O maior número é:', result)