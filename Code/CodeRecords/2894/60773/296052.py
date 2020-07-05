num=int(input())
s=input()
sum=0
for i in range(num-1):
    if s[i:i+2]=='VK':
        sum=sum+1
if "VVV" in s or "KKK" in s:
    sum=sum+1
else:
    if s=="VV" or s=="KK":
        sum=sum+1
print(sum,end="")
    