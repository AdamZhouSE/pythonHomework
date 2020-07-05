n = input()
strr = input()
strt = strr.split(',')
str = []
for j in strt:
    str.append(int(j))
str = sorted(str)
#print(str,n)
out = 0
for le in range(1,len(str)):
    for op in range(len(str)+1):
        if out==1:
            break
        if op+le > len(str):
            break
        sum = 0
#        print(str[op:op+le])
        for i in str[op:op+le]:
            sum = sum + int(i)
        if sum >= int(n):
            print(le)
            out = 1
if out==0:
    print(6)