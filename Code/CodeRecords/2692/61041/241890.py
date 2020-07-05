strin = input()
days = input()
intarr = []
i=0
while i<len(strin):
    if strin[i]=='[' or strin[i]==']' or strin[i]==',':
        i = i + 1
        continue
    temp1 = strin[i]
    while strin[i+1]!=',' and strin[i+1]!=']':
        temp1 = temp1 + strin[i+1]
        i = i + 1
    intarr.append(int(temp1))
    i = i + 1
temp = 0
for j in range(0,len(intarr)):
    temp = temp + intarr[j]
temp = temp//int(days)
cnt = 0
x = 0
y = 0
while True:
    while y<len(intarr):
        while y<len(intarr) and x+intarr[y]<=temp:
            x = x + intarr[y]
            y = y + 1
        x = 0
        cnt = cnt + 1
    if cnt==int(days):
        break
    else:
        cnt = 0
        x = 0
        y = 0
        temp = temp + 1
print(temp)