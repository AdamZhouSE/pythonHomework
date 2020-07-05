x = int(input())
y = int(input())
ans = 0
while y>x:
    ans+=1
    if y%2==1:
        y+=1
    else:
        y=y//2
print(ans + x-y)