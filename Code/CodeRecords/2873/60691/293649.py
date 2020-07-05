s1 = input()
s2 = input().split(" ")
s3 = input().split(' ')

lsource = []
lfinger = []
for i in range(len(s2)):
    lsource.append(s2[i])
for i in range(len(s3)):
    lfinger.append(s3[i])

lresult = []

for i in lsource:
    if i in lfinger:
        lresult.append(i)
        
for i in range(len(lresult)-1):
    print(lresult[i], end='')
    print(' ', end='')
print(lresult[len(lresult)-1])