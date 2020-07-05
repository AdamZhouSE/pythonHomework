s = input()
dic = {}
li = list(s)
Set = set(s)
for ele in Set:
    dic[ele] = li.count(ele)

res = sorted(dic.items(),key=lambda x:x[1],reverse=True)

for ele in res:
    for i in range(int(ele[1])):
        print(ele[0],end="")
print("")