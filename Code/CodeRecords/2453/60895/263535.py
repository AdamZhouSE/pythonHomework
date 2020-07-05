s=input().split(',')
k=int(input())
result=False
for i in range(0,len(s)):
    if s[i]==str(k):
        result=True
        break
print(result)