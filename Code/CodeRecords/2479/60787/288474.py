t=int(input())
for ex in range(0,t):
    a=list(input())
    b=list(input())
    re=[]
    for i in range(0,len(a)):
        if not a[i] in b:
            re.append(a[i])
    for i in range(0,len(b)):
        if not b[i] in a:
            re.append(b[i])
    re=sorted(list(set(re)))
    print("".join(re),end="\n\n")