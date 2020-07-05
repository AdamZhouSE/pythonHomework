n=input()
n=int(n)
ls=input().split(" ")
ls=[int(ls[i]) for i in range(n)]
c=0
for i in range(1,n-1):
    if (ls[i]-ls[i-1])*(ls[i]-ls[i+1])>0:
        print(-1)
        break
ls1=[0]*n
for j in range(n):
    if ls[j]>ls[j+1]:
        print(n-j-1)
        break
