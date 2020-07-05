i = input()
dic = {}
for j in i.split(','):
    dic[j] = dic.get(j,0) + 1
for k in dic.keys():
    if dic[k] > 1:
        print(k)