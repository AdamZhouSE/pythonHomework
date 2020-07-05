n=int(input())
s=input()
ls=[]
for i in range(n):
    ls.append(s[i])

result=0
i=0
while i <=len(ls)-2:
    if ls[i]==ls[i+1]:
        result=result+1
        del ls[i]
    else:
        i=i+1

print(result)