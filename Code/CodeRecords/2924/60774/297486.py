def getKey(elem):
    return elem[1]

s = input().split(' ')
n = int(s[0])
r = int(s[1])
avg = int(s[2])
a = []
target = avg * n
for i in range(0,n):
    s = input().split(' ')
    target = target - int(s[0])
    a.append([int(s[0]),int(s[1])])
if(target <= 0):
    print(0)
else:
    a.sort(key = getKey)
    count = 0
    for item in a:
        if(item[0] < r):
            if(target <= r - item[0]):
                count = count + target * item[1]
                break
            else:
                count = count + (r - item[0]) * item[1]
                target = target - (r - item[0])
    print(count)