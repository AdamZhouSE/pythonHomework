string=str(input())
res=''
for i in range(len(string)):
    res+=string[i]
for i in range(len(string)-1,-1,-1):
    res+=string[i]
print(res)