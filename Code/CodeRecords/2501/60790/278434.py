n=int(input())
t1=input().split()
t2=input().split()
count=0
def func(i,j):
    left=t1[i]
    right=t1[j]
    l1=t2.index(left)
    r1=t2.index(right)
    if(r1<l1):
        return True
    else:
        return False
for i in range(0,n):
    for j in range(i+1,n):
        if(func(i,j)):
            count+=1
print(count)