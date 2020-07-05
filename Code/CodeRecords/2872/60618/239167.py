n=int(input())
s=list(input())
num=0
for i in range(0,n-1):
    if s[i]==s[i+1]:
        num=num+1
print(num)  