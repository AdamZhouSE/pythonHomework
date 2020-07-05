num = int(input())
str = input().split(' ')
lists =[int(i) for i in str]
check = False
for i in range(1,num+1):
    a = lists[i-1]
    b = lists[a-1]
    c = lists[b-1]
    if c==i:
        check = True
        break
print("YES") if check else print("NO")
