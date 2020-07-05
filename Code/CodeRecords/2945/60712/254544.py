s = list(input())
sumOfb=0
sumOfo=0
sumOfy=0
for i in range(len(s)):
    if s[i]=='b':
        sumOfb+=1
    if s[i]=='o':
        sumOfo+=1
    if s[i]=='y':
        sumOfy+=1
print(max(sumOfb,sumOfo,sumOfy))
sumOfg=0
sumOfi=0
sumOfr=0
sumOfl=0
for i in range(len(s)):
    if s[i]=='g':
        sumOfg+=1
    if s[i]=='i':
        sumOfi+=1
    if s[i]=='r':
        sumOfr+=1
    if s[i]=='l':
        sumOfl+=1
print(max(sumOfg,sumOfi,sumOfr,sumOfl))
