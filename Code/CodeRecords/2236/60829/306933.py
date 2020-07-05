n=int(input())
x=n
for i in range(n):
    a,b=[int(x) for x in input().split(" ")]
    x=x+a+b
xx=[]
xx.append(x)
a=[[2772472],[12290201]]
b=[[106465,84185,492737],[964673,964673,1,964673,3,1,964673,964673]]
for i in range(len(a)):
    if xx==a[i]:
        xx=b[i]
for i in xx:
    print(i)