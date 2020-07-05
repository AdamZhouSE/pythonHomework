n = int(input())
ans = []
name_list = []
check_list = []
for i in range(n):
    name_list.append(input())
m = int(input())
for i in range(m):
    name = input()
    if name in check_list:
        ans.append('REPEAT')
        continue
    elif name in name_list:
        ans.append('OK')
        check_list.append(name)
        continue
    else:
        ans.append('WRONG')
for i in ans:
    print(i)
