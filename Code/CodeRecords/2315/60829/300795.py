def find(a,k):
    for i in range(len(a)):
        if a[i]==k:
            return i
    return -1
a=[]
n=int(input())
for i in range(pow(2,n)-1):
    a.append(-1)
