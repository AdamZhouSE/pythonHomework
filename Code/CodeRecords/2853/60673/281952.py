
inp = int(input())
cookies=input().split(" ")
for i in range(inp):
    cookies[i]=int(cookies[i])
sum=0
odd=0
for x in cookies:
    sum+=x
    if(x%2==1):
        odd+=1
if(sum%2==1):
    print(odd)
else:
    print(inp-odd)