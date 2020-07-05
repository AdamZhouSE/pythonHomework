a=float(input())
n=int(input())
count=1.0;flag=1
if(n<0):
    n=-n
    flag=-1
for i in range(n):
    count*=a
if(flag==-1):
    count=1/count
print("{:.5f}".format(count))