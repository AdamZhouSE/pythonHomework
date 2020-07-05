a=input()
b=input()

ans=0
for i in range(0,len(a)-len(b)+1):
    
    if a[i:i+3]==b:
        ans+=1
print(ans)