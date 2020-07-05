str = input()
state = str[0]
res = 0
for i in range(0,len(str)):
    if str[i]==state:
        continue
    else:
        res+=1
        state = str[i]
if state=='1':
    print(res,end='')
else:
    print(res+1,end='')