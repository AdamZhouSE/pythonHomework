n,x=map(int(input().split()))
chapter=input().split()
chapter.sort()
result=0
for i in range(0,n):
    result=result+int(chapter[i])*x
    if x>=2:
        x -= 1
print(result)