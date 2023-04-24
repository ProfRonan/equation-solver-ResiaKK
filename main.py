numero = int(input("Digite o numero que indica grau da equação:  "))


if numero>2:
    print("Grau inválido")

if numero<0:
    print("Grau inválido")

if numero==1:
    print("A equação é do primeiro grau")
    
    a = int(input("Digite o valor de a:  "))
    if a==0:
       print("Valor de a inválido ")
        
        
    else:
       b = int(input("Insira o valor de b:  "))

       raiz_primeiro = -(b) / a

       print("{:.2f}".format(raiz_primeiro))

if numero==2:
    print("A equação é do segundo grau")

    a = int(input("Digite o valor de a:  "))
    if a==0:
        print("Valor de a inválido")

    else:
        b = int(input("Digite o valor de b:  "))
        c = int(input("Digite o valor de c:  "))
        StopIteration

delta = b**2 - 4 * a *c 
raiz_linha = (-b + delta**0.5) / (2*a)
raiz_linhas = (-b - delta**0.5) / (2*a)
raiz_unica = (-b) / (2*a)
if delta<0:
    print("A equação não possui raízes reais")   

elif delta==0:
    print("A equação possui apenas uma raiz real")
    print("{:.2f}".format(raiz_unica)) 

elif delta>0:
    print("A equação possui duas raízes reais")
if raiz_linha < raiz_linhas:
    print("{:.2f}, {:.2f}".format(raiz_linha, raiz_linhas))
else:
    print("{:.2f}, {:.2f}".format(raiz_linhas, raiz_linha))