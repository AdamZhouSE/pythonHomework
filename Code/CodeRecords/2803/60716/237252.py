n,m = map(int, input().split())
listmagic = []
listlamp = []
for i in range(n):
    str = input().split(' ')
    list = [int(i) for i in str]
    listmagic.append(list[0])
    for j in range(1,len(list)):
        listlamp.append(list[j])
sets = set(listlamp)
check = True
for i in range(1,m+1):
    if not i in sets:
        check = False
        break
print("YES") if check else print("NO")