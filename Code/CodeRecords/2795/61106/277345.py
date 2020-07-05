n=int(input())
s=input().split()
diff,result=0,0
for i in range(n):
    s[i]=int(s[i])
s.sort()
test=[s[0]]
for i in range(n-1):
    if s[i+1]!=s[i]:
        test.append(s[i+1])
if len(test)>3:
    result=-1
elif len(test)==3:
    if test[2]-test[1]!=test[1]-test[0]:
        result=-1
    else:
        result=test[2]-test[1]
elif len(test)==2:
    result=test[1]-test[0]
    if result%2==0:
        result=result//2
else:
    result=0
print(result)