n = int(input())
dic = {}
for i in range(n):
    str = input()
    if str in dic:
        dic[str] += 1
    else:
        dic[str] = 1
l = list(dic.values())
l.sort(reverse=True)
print (l[0])