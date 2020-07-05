n=(int)(input())
for index in range(0,n):
    x=(int)(input())
    temp=1
    while temp*temp*temp<=x:
        temp+=1
    print(temp-1)