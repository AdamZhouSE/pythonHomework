T=int(input())
for i in range(0,T):
    num=int(input())
    numbin=bin(num)[2:]
    one=0
    for j in range(0,len(numbin)):
        if numbin[j]=='1':
            one=one+1
    if one%2==0:
        print("even")
    else:
        print("odd")
