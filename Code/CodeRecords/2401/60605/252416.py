label = int(input())
begin = 0
while not(pow(2, begin) <= label < pow(2, begin+1)):
    begin += 1
begin += 1

targetLevel = begin
if targetLevel % 2 == 0:
    label = pow(2, begin-1)+pow(2, begin)-1-label
outli = []
tl = label
while targetLevel > 0:
    ttl = tl
    if targetLevel % 2 == 0:
        ttl = pow(2, targetLevel-1)+pow(2, targetLevel)-1-ttl
    outli.insert(0, ttl)
    tl //= 2
    targetLevel -= 1
print(outli)