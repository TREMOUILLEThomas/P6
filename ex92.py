a=int(input("quel nombre ? : "))
i=0
vmax=1
while a>1:
    if a%2==1:
        a=a*3+1
    else:
        a=a//2
    print(a)
    i=i+1
    if a>vmax:
        vmax=a
print("le nb d'étapes est :" ,i,)
print("le plus grand est :",vmax,)