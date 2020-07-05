t=int(input())
for ex in range(0,t):
    n=int(input())
    s=list(input())
    print(s)
    while "," in s:
        s.remove(",")
    string="".join(s)
    print(string)
    num=[int(i) for i in string.split(" ")]
    a,b,c,d=-1,-1,-1,-1
    for i in range(0,len(num)-1):
        for j in range(i+1,len(num)):
            temp=num[i]+num[j]
            for p in range(i+1,len(num)-1):
                for q in range(p+1,len(num)):
                    if temp==num[p]+num[q] and not (p==j or q==j):
                        a,b,c,d=i,j,p,q
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    if -1 in [a,b,c,d]:
        print("no pairs")
    else:
        print(a,b,c,d)