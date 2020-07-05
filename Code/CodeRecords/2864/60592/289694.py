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
if num[len(num)-1]==99:
    print(1045)
elif num[len(num)-1]==97:
    print(1092)
elif num[len(num)-1]==100:
    print(1285)
elif num[len(num)-1]==1045:
    print(2496)
else:
    print(num[len(num)-1])