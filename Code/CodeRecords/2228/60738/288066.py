num=int(input())
index=0
if num<0:
    num=-num
def summ(n):
    res=0
    for i in range(1,n+1):
        res+=i
    return res
for j in range(1,10):
    for k in range(0,j):
        if summ(j)-2*k==num:
            index=j
            break
    if index==j:
        break
print(index)
if index==1:
    print(num)