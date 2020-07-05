num=int(input())
num1=0
for i in range(2,num+1):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
    if flag:
        num1+=1
num2=num-num1
def func(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*func(n-1))
res=(func(num1)*func(num2))%(10**9+7)
print(res)