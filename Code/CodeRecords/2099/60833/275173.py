s=str(input())
n=len(s)
s1=s[::-1]
result=0
for i in range(0,n):
    a=ord(s1[i])-ord('A')+1
    result=result+(26**i)*a
print(result)