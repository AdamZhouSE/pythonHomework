num=int(input())
sqr=False
for i in range(num+1):
    if(i**2==num):
        sqr=True
        break
        
print(sqr)