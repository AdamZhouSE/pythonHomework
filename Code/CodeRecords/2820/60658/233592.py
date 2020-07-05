n = int(input())
dic = {}
for i in range(n):
    ti = input()
    if ti in dic:
        dic[ti]+=1
    else:
        dic[ti]=1
print(max(dic.values()))