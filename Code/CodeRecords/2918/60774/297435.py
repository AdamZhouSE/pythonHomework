n = int(input())
press = list(map(int,input().split(' ')))
press.sort(reverse = True)
temp = 0
base = 0
for i in range(0,n):
    temp = temp + press[i]
    if(temp > n):
        base = i + 1
        break
else:
    base = n
if(base != n):
    pileLst = press[:base]
    press = press[base:]
else:
    print(n)
