t = int(input())
for i in range(t):
    l, r = map(int,input().split(" "))
    res= 0
    for k in range(l,r+1):
        if  k<10:
            res+=1
            continue
        if str(k)[0] == str(k)[-1]:
            res+=1
    print(res)