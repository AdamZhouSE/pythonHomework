s=input()
l=len(s)
result=0
for i in range(0,l):
    n=int(ord(s[i])-ord('A'))+1
    temp=1
    for j in range(0,l-i-1):
        temp=temp*26
    result=result+n*temp
print(result)