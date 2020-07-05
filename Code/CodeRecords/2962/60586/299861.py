def exam16():
    x=input().split(" ")
    n,p=int(x[0]),int(x[1])
    counter=[]
    string=[i for i in input().split(" ")]
    alph=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for item in string:
        l=len(item)
        inter=alph.index(item[l-1])+alph.index(item[l-2])*2**5+alph.index(item[l-3])*2**10
        loc=inter%p
        if counter.count(loc)>0:
            probe=counter.count(loc)
            while loc==0:
                loc=loc+probe**2
                probe+=1
                if loc>p:
                    loc=loc%p
        counter.append(loc)
    for i in range(len(counter)-1):
        print(counter[i],end=" ")
    print(counter[len(counter)-1])

exam16()    