n = input()
s = input().split()
s = list(map(int,s))

 

a = list(range(0,4))
for i in range(0,4):
    a[i] = 0
taxi = 0
for i in range(0,len(s)):
    if (s[i] == 1):
        if (a[1] > 0):
            a[1] -= 1
        else:
            a[3] += 1
            taxi += 1
    elif (s[i] == 2):
        if (a[2] > 0):
            a[2] -= 1
        else:
            a[2] += 1
            taxi += 1
    elif (s[i] == 3):
        if (a[3] > 0):
            a[3] -= 1
        else:
            a[1] += 1
            taxi += 1
    elif (s[i] == 4):
        taxi += 1 
if (a[3] > a[2]):
    taxi -= (a[2]*2)
    a[3] -= (a[2]*2)
    taxi -= (a[3] // 4) * 3
    a[3] = a[3]%4
    if (a[3] < 4 and a[3] > 1):
        taxi -= a[3]-1
else:
    taxi -= a[3]
print(taxi)