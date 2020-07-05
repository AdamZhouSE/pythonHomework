a=int(input())
b=list(input())
bb=[x for x in b if str(x).isdigit()]
x=""
for i in bb:
    x=x+str(i)
sum=1
for i in range(0,int(x)):
    sum=a*sum
print(sum%1337)