n,x=input().split()
n,x=int(n),int(x)
chapter=input().split()
for i in range(len(chapter)):
    chapter[i]=int(chapter[i])
chapter.sort()
result=0
for i in range(0,n):
    result=result+int(chapter[i])*x
    if x>=2:
        x -= 1
print(result)