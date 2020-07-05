n,k=input().split(' ')
n=int(n)
k=int(k)
last=''
while n>0:
    name,index=input().split(' ')
    last=name+last
    n=n-1
while k>0:
    interst=input()
    length=len(interst)
    num=0
    for i in range(0,len(last)-length+1):
        na=last[i:i+length]
        if interst==na:
            num=num+1
    print(num)
    k=k-1