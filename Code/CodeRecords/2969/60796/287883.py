s=input()
result=[]
for i in range(1,len(s)):
    if s[i]<=s[i-1]:
        result.append(i)
if len(s)==1:
    result=[1]
for i in range(len(result)):
    print(result[i],end=' ')
