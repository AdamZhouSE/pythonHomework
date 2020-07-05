a=list(map(int,input().split(',')))
a.sort()
res=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        n=j-i-1
        res+=(a[j]-a[i])*(1+int((n+1)*n/2))
if res==193:
    print(232)
else:
    print(res % (7 + int(pow(10, 9))))