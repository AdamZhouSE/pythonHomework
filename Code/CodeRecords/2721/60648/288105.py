n=int(input())
for i in range(n):
    s,x=input().split(' ')
    c=1
    w,e=0
    for j in range(len(s)):
        w+=c*int(s[-1-j])
        c*2
    c=1
    for k in range(len(x)):
        e+=c*int(x[-1-k])
        c*2
    print(w*e)