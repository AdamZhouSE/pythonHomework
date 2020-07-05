n=input()
n=int(n)
ls=input().split(" ")
ls=[int(ls[i]) for i in range(n)]
lsr=[0]*n
for i in range(n):
    lsr[ls[i]-1]=str(i+1)
print(" ".join(lsr))