n=int(input())
for i in range(n):
    s,x=input().split(' ')
    #print(s)
    #print(x)
    #print(ss)
    c=1
    w,e=0,0
    for j in range(len(s)):
        w+=c*int(s[-1-j])
        #print(w)
        c=c*2
    c=1
    for k in range(len(x)):
        e+=c*int(x[-1-k])
        c=c*2
    print(w*e)