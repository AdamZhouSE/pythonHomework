# 广度搜索 复杂
# 逆向思维 乘2总是比+1更容易接近目标

x = int(input())
y = int(input())
ans = 0
if x>=y:
    print(x-y)
else:
    while y > x:
        ans+=1
        if y%2 == 1:
            y+=1
        else:
            y//=2
    print(ans+x-y)
        