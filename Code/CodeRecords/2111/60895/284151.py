n=int(input())
result=n
i=2
while i<=result:
    temp=i
    ifchou='True'
    while temp>1:
        if temp%2==0:
            temp=temp//2
        elif temp%3==0:
            temp=temp//3
        elif temp%5==0:
            temp=temp//5
        else:
            ifchou='False'
            break
    if ifchou=='False':
        result=result+1
    i=i+1
print(result)