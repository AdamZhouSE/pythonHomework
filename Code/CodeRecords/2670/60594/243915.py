def two(n:int)->int:
    temp=1
    for index in range (0,n):
        temp*=2
    return temp

n=(int)(input())
for index in range(0,n):
    x=(int)(input())
    temp=1
    while two(temp)<x:
        temp+=1
    print(two(temp)-1-x)