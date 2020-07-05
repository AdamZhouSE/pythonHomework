s = input().split(' ')
n = int(s[0])
m = int(s[1])
temp = m
a = []
for i in range(0,n):
    s = list(map(int,input().split(' ')))
    m = m - s[0]
    temp = temp - s[1]
    a.append(s[0] - s[1])
if(m >= 0):
    print(0)
elif(temp < 0):
    print(-1)
else:
    a.sort(reverse = True)
    for j in range(0,n):
        m = m + a[j]
        if(m >= 0):
            print(j + 1)
            break