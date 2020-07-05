element = input().split(' ');
s = [int(i) for i in element]
lists = []
for i in range(s[1]):
    key = int(input())
    lists.append(key)

index = 0
mods = s[0]
List = []
check = False
for i in range(s[1]):
    index+=1
    temp = lists[i]%mods
    if temp in List:
        check = True
        break;
    else:
        List.append(temp)
print(index) if check else print(-1)