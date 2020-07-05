s=input()
l=len(s)
result=0
for i in range(l,0,-1):
    n=ord(s[l-i]-'A')+1
    temp=1
    for j in range(0,n):
        temp=temp*26
    result=result+temp
print(result)