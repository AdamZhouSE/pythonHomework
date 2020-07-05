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
print(num[0][0])

