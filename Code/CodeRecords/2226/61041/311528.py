left=eval(input())
right=eval(input())
res=[]
for i in range(left,right+1):
    temp=i
    j=0
    while temp!=0:
        div=temp%10
        if div==0:
            j=1
            break
        if i%div!=0:
            j=1
            break
        temp=temp//10
    if j==0:
        res.append(i)
print(res)