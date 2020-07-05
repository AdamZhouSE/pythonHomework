num = int(input())
listsfortime = []
listsfornum = []
for i in range(num):
    str = input()
    if str in listsfortime:
        listsfornum[listsfortime.index(str)]+=1
    else:
        listsfortime.append(str)
        listsfornum.append(1);
listsfornum.sort()
listsfornum.reverse()
print(listsfornum[0])