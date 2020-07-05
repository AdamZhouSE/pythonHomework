str1=input().split()
n=int(str1[0])
x=int(str1[1])
ci=input().split()
ci=list(map(int,ci))
ci.sort()
count=0
for i in range (0,n):
    if(x>1):
        count=count+x*ci[i]
        x=x-1
    else:
        count=count+x*ci[i]
print(count)