pres = list(map(int,input().split(' ')))
data = list(map(int,input().split(' ')))
lim = pres[1]
cou = pres[2]
res = 0
for i in range(0,len(data)-cou+1):
    tem = data[i:i+cou]
    tem.sort()
    if tem[cou-1]<=lim:
        res+=1
print(res)