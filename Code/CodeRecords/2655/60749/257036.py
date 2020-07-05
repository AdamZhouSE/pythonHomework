n=int(input())
res=[]
for _ in range(n):
    res.append(int(input()))
def findcloset(n):
    k=0
    while n>=pow(2,k):
        if n<pow(2,k+1):
            if n==pow(2,k):

                return pow(2,k)
            else:
                return pow(2,k+1)
        k+=1
for t in res:
    print(findcloset(t), end=" \n")
print()