s=input().split(',')
result=-1
for i in range(1,len(s)-1):
    if int(s[i])>int(s[i+1]) and int(s[i-1])<int(s[i]):
        result=i
        break
if result==-1:
    if int(s[0])>int(s[len(s)-1]):
        result=0
    else:
        result=len(s)-1
print(result)