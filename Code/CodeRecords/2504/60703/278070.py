def distance(a:list):
    return a[0]*a[0]+a[1]*a[1]

points = eval(input())
K = int(input())
dic = dict()
for i in points:
    dic[(i[0],i[1])] = distance(i)
ress = list(dic.items())
ress.sort(key = lambda x:x[1])
#print(ress)
res = []
for i in range(K):
    res.append([ress[i][0][0],ress[i][0][1]])
print(res)