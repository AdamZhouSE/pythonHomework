num = int(input())
str = input().split(' ')
lists =[int(i) for i in str]
check = False
for i in range(num):
    a = list[i]
    b = list[a]
    c = list[b]
    if c==i:
        check = True
        break
print("YES") if check else print("NO")
