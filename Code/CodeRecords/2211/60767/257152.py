def getNames(names):
    res = []
    for i in range(0,len(names)):
        if(int(names[i][1])==0):
            res.append(names[i][0])
        else:
            res.append(names[i][0]+res[int(names[i][1])-1])
    return res

def ans(names,target):
    cnt = 0
    for name in names:
        if(name.startswith(target)):
            cnt+=1
    return cnt

temp = input().split(" ")
n = int(temp[0])
k = int(temp[1])
names = []
test = []
for i in range(n):
    names.append(input().split(" "))
for x in range(k):
    target = input()
    test.append(target)
    res = ans(getNames(names),target)
    print(res)
