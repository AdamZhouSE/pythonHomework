list=input().split()
n=int(list[0])
x=int(list[1])
ci=input().split()
for i in range(n):
    ci[i]=int(ci[i])
ci.sort()
count=0
for time in ci:
    count=count+int(time)*x
    if(x>1):
        x=x-1
print(count)