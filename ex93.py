def nb():
    nba=0
    nbb=0
    nemax = 0
    vmaxmax = 0
    for k in range(1,21):            
        a=k
        i=0
        vmax=a
        while a>1:
            if a%2==1:
                a=a*3+1
            else:
                a=a//2
            i=i+1
            if a>vmax:
                vmax=a
        if i>nemax:
            nemax=i
            nba=k
        if vmax>vmaxmax:
            vmaxmax=vmax
            nbb=k
        print("le nb d'étapes est pour :",k, "est:" ,i,)
        print("le plus grand est :",k,"est" ,vmax)
        print()
    print("le plus grand nb d'étapes est :" ,nemax, "pour", nba)
    print("le plus grand nb est :",vmaxmax, "pour",nbb)