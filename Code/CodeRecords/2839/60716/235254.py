num = int(input())
list = []
check = []
for i in range(num):
    name = input()
    if name in list:
        check.append("YES")
    else:
         check.append("NO")
         list.append(name)
for i in check:
    print(i)