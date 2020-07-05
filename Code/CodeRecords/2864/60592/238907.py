total = int(input())
data = list(map(int,input().split(' ')))
data.sort()
catg = []
for i in range(0,total):
    if data[i] in catg:
        continue
    else:
        catg.append(data[i])
num = [0]*len(catg)
for i in range(0,len(catg)):
    num[i] = data.count(catg[i])*catg[i]
print(data)
print(num)
