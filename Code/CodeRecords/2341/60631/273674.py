t=int(input())
for ti in range(t):
    input()
    a=input().split(' ')
    b=input().split(' ')
    ai=[]
    for i in a:
        ai.append(int(i))
    bi=[]
    for i in b:
        bi.append(int(i))
    ci=sorted(ai+bi)
    for j in ci:
        print(j,end=' ')
    print()