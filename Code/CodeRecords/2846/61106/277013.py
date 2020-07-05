n=int(input())
code=input().split()
result=len(code)
for i in range(len(code)):
    code[i]=int(code[i])
code.sort()
for i in range(len(code)-1):
    if code[i]==code[i+1]:
        result -= 1
if 0 in code:
    result -= 1
print(result)