num=int(input())
while(num>1):
    if num%2==0:
        num=num/2
    else:
        break
print(num==1)