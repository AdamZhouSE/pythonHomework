n = int(input())
modeLst = []
for i in range(0,n):
    mode = input()
    modeLst.append(mode)
s = input()
rec = ['',0]
for m in modeLst:
    count = 0
    for i in range(0,len(s) - len(m) + 1):
        temp = s[i: i + len(m)]
        if(temp == m):
            count = count + 1
    if(count > rec[1]):
        rec[0] = m
        rec[1] = count 
print(rec[1])
print(rec[0])