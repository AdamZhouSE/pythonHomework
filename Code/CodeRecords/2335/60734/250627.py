import re
lst = re.findall(r'\d+',input())
x = int(lst[0])
y = int(lst[1])

#逆向计算  +1 /2
count = 0
while y!=x:
    if y<x:
        y += 1
    else:
        if y%2==0:#偶数
            y /= 2
        else:
            y+=1
    count+=1
print(count)