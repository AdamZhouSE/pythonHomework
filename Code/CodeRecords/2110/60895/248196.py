num=int(input())
result='True'
while num>1:
    if num%2==0:
        num=num//2
    elif num%3==0:
        num=num//3
    elif num%5==0:
        num=num//5
    else:
        result='False'
        break
print(result)