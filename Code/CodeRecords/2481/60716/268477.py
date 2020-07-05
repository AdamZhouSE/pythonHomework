ucnum = int(input())
ans = list()
for i in range(ucnum):
    n,m = map(int,input().split())
    str1 = input().split()
    str2 = input().split()
    list1 = [int(k) for k in str1]
    list2 = [int(k) for k in str2]
    temp = list1.copy()
    temp.extend(list2)
    temp = list(set(temp))
    index = 0
    for j in temp:
        if j in list1 and j in list2:
            index+=1
    ans.append(index)
for i in ans:
    print(i)
