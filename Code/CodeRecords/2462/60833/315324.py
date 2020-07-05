s=input().split(',')
res=-1
for i in range(1,len(s)-1):
    if int(s[i])>int(s[i+1]) and int(s[i-1])<int(s[i]):
        res=i
        break
if res==-1:
    if int(s[0])>int(s[len(s)-1]):
        res=0
    else:
        res=len(s)-1
print(res)