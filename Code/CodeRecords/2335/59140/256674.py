x = int(input())
y = int(input())
if x >= y:
    print(x - y)  # 递减
elif y%2==0:
    temp = 0
    while x < y // 2:
        x *= 2
        temp+=1
    temp+=x-y//2+1
    print(temp)
else:
    temp = 0
    while x < y //2 +1:
        x *= 2
        temp += 1
    temp += x - y // 2 +1
    print(temp)