s=input().split(',')
k=int(input())
result=-1
for i in range(0,len(s)):
    if s[i]==str(k):
        result=i
        break
print(result)