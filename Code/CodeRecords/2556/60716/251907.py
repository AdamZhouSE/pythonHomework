def checkrepeat(x,y):
    for j in range(len(lists)):
        temps = lists[j]
        a = temps[0]
        b = temps[1]
        if (a-k<x and a+k>x)and(b-k<y and b+k>y):
            t = list()
            t.append(a)
            t.append(b)
            t.append(x)
            t.append(y)
            repeat.append(t)

def calcuarea():
    a = repeat[0][0]
    b = repeat[0][1]
    x = repeat[0][2]
    y = repeat[0][3]
    k1 = k - abs(x-a)
    k2 = k - abs(y-b)
    return k1*k2

n,k = map(int,input().split())
lists = list()
repeat = list()
for i in range(n):
    a,b = map(int,input().split())
    checkrepeat(a,b)
    templist = list()
    templist.append(a)
    templist.append(b)
    lists.append(templist)
#print(lists)
#print(repeat)
if len(repeat)==0:
    print("0")
elif len(repeat)==1:
    temp = calcuarea()
    print(temp)
else:
    print("-1")