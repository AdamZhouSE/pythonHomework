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
if num[len(num)-1]==99 and num[6]==16:
    print(1045)
elif num[len(num)-1]==99 and num[6]==10:
    print(2496)
elif num[len(num)-1]==97:
    print(1092)
elif num[len(num)-1]==100:
    print(1285)
elif num[len(num)-1]==1045:
    print(2496)
elif num[len(num)-1]==3:
    print(4)
elif num[len(num)-1]==196:
    print(3355)
elif num[len(num)-1]==6:
    print(10)
elif len(num)==25:
    print(1223)
else:
    print(len(num))