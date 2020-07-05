n=int(input())
for q in range(n):
    x=input().split()
    s1=int(x[0])
    s2=int(x[1])
    x1=input().split()
    x2=input().split()
    tmp=[]
    for i in x1:
        tmp.append(int(i))
    for i in x2:
        tmp.append(int(i))
    tmp.sort()
    for i in range(s1):
        print(tmp[i],end=' ')
    
    for i in range(s1,s1+s2):
        print(tmp[i],end=' ')
    print()
             