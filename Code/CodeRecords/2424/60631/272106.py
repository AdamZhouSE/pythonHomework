t=int(input())
for ti in range(t):
    n=int(input())
    s=input().split(' ')
    p=[]
    for i in s:
        p.append(int(i))
    s=sorted(p)
    s.append(-1)
    #print(s)
    for j in range(n):
        if j%2!=0:
            continue
        if s[j]!=s[j+1]:
            print(s[j])
            break