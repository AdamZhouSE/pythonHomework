s=str(input())
i=len(s)-1
b=""
while i>=0:
    b=b+s[i]
    i-=1
    
print(s+b)