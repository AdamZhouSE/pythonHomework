a=eval(input())
#print(a[0])

m=a[0]
n=a[1]

count=0
while m!=n:
    m>>=1
    n>>=1
    count=count+1
    
n<<=count
print(n)