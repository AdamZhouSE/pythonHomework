#27
n = int(input())
dic = {}
name = []
for i in range(0,n):
    ori = input().split(" ")
    name.append(ori[0])
    if ori[0] not in dic:
        dic[ori[0]] = int(ori[1])
    else:
        dic[ori[0]] += int(ori[1])
num = sorted(dic.items(),key=lambda x:x[1],reverse=True)
# nameSort = sorted(dic,reverse=True)
# print(dic)
if num[0][1] == num[1][1]:
    name1 = num[0][0]
    name2 = num[1][0]
    temp = name[name.index(name2):]
    if name1 in temp:
        print(num[1][0])
    else:
        print(num[0][0])
else:
    print(num[0][0])