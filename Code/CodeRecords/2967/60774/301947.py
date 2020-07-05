n = int(input())
sLst = []
for i in range(0,n):
    sLst.append(input())
sLst.sort(key = lambda x:len(x))
base = sLst[0]
max = 0
for i in range(0,len(base) - 1):
    for j in range(i + 1,len(base) + 1):
        temp = base[i:j]
        for s in sLst:
            if(temp not in s):
                break
        else:
            if(len(temp) > max):
                max = len(temp)
print(max)