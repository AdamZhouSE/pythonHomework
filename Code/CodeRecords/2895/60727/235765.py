a= input()
c = len(a)
a= a[1:c-1]
l=a.split(",")

m=int(l[0])
n=int(l[1])
while m<n:
    n = n & (n-1)
print(n)
       