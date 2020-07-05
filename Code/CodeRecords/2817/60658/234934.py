n = int(input())
li = [int(x)-1 for x in input().split()]
flag = False
for i in li:
    if li[li[li[i]]]==i:
        flag=True
        break
print("YES" if flag else "NO")
    