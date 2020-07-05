t=int(input())
for ti in range(t):
    input()
    s=input().split(' ')
    ss=[]
    for i in s:
        ss.append(int(i))
    ss=sorted(ss)
    for j in range(len(ss)-1):
        print(ss[j],end=' ')
    print(ss[-1],end='')
    print()