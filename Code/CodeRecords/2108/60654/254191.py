a = int(input())
sum = 0
while a != 0:
    if a%10== 0:
        sum += 1
    else:
        sum += a%10 
    a = a//10    
print(sum)        