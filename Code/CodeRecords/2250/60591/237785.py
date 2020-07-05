def keys(temp):
    return temp[0]

def do(num):
    num *= 2
    for x in range(1,num):
        if(x * (x+1)== num):
            return x

def getLine(list):
    list.sort(key = keys)
    i = j = 0
    result = []
    a = 0
    b = 0
    while(i < len(list)):
        j = i + 1
        while(j < len(list)):
            x = list[j][1] - list[i][1]
            y = list[j][0] - list[i][0]
            if(x == 0):
                a += 1
            elif(y==0):
                b += 1
            else:
                k = x/y
                m = list[j][1] - k*list[j][0]
                result.append((k,m))
            j = j + 1
        i = i + 1
    result.sort(key=keys)
    c = 1
    max1 = 1
    pre = result[0]
    for i in range(1,len(result)):
        if(result[i][1]==pre[1]):
            c += 1
            pre = result[i]
        else:
            if (c > max1):
                max1 = c
            c = 1
            pre = result[i]
    if(c > max1):
        max1 = c
    max1 = do(max1)
    return max(a,b,max1 + 1)

n = eval(input())
temp = []
while( n != 0):
    n = n - 1
    temp.append(list(map(int,input().split(","))))
print(getLine(temp))