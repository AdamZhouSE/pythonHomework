def c(n):
    count=0
    if n%5==0:
        count=count+1
        n=n//5
    return count
a=int(input())
coun=0
for i in range(2,a+1):
    coun=coun+c(i)
print(coun)
