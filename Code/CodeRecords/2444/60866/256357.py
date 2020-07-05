def paixu(a,k,t):
    for i in range(0,len(a)-t):
        if a[i]-a[i+t]==k or a[i]-a[i+t]==-k:
            print('true')
            return
    print('false')
a=input()
a=eval(a)
k=int(input())
t=int(input())
paixu(a,k,t)