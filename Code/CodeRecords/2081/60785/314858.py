a=input()
b=input()
print(a,b)
ans=0
for i in range(0,len(a)-len(b)+1):
    print(a[i:i+3])
    if a[i:i+3]==b:
        ans+=1
print(ans)