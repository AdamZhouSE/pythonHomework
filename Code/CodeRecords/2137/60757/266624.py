n=int(input())
li=[]
for i in range(1,n):
    if n%i==0:
        li.append(i)
count=0
for i in range(len(li)):
    count=count+li[i]
if count==n:
    print(True)
else:
    print(False)
    