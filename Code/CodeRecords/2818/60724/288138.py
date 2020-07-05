one=input().split(" ")
n=int(one[0])
x=int(one[1])
time=0
chapter=input().split(" ")
for i in range(n):
    chapter[i]=int(chapter[i])
chapter.sort()
for i in range(n):
    time=time+x*chapter[i]
    if x>1:
        x=x-1
print(time)