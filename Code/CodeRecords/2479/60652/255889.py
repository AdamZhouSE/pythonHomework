T=int(input())
for i in range(0,T):
    s1=input()
    s2=input()
    l=[]
    for m in s1:
        if m not in s2 and m not in l:
            l.append(m)
    for n in s2:
        if n not in s1 and n not in l:
            l.append(n)
    l.sort()
    print("".join(str(i) for i in l))
    print()