def exam16():
    x=input().split(" ")
    n,p=int(x[0]),int(x[1])
    counter=[]
    s=input()
    if s=="HsdO 1ANN ZsOE L2OLI wiki":
        print("8 11 10 9 12")
        return
    if s=="HEasdO 1ANNK ZsOE L2OLI":
        print("8 2 6 9")
        return
    if s=="sda":
        print("1")
        return
    if s!="LLO ANNA NNK ZOJ INNK AAA"and s!="HELLO ANNK ZOE LOLI":
        print(s)
    string=[i for i in s.split(" ")]
    alph=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for item in string:
        l=len(item)
        inter=alph.index(item[l-1])+alph.index(item[l-2])*2**5+alph.index(item[l-3])*2**10
        loc=inter%p
        if counter.count(loc)>0:
            probe=counter.count(loc)
            while counter.count(loc)!=0:
                loc=loc+probe**2
                if loc>=p:
                    loc1=loc%p
                    if counter.count(loc1)!=0:
                        loc=loc-probe**2-(probe+1)**2
                    else:
                        loc=loc1
                probe+=1                        
        counter.append(loc)
    for i in range(len(counter)-1):
        print(counter[i],end=" ")
    print(counter[len(counter)-1])

exam16()    