n=int(input())
for i in range(n):
    s=list(input())
    ind=[]
    l=[]
    now=1
    for i in range(len(s)):
        if s[i]=='(':
            ind.append(now)
            print(now,end=" ")
            now+=1
        elif s[i]==')':
            print(ind[-1],end=" ")
            ind.pop()
           # print(ind)
    print()