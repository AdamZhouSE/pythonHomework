def gcd(a,b):
    if b==0:return a
    return gcd(b,a%b)

arr = input().split(",")
for i in range(len(arr)): arr[i] = int(arr[i])
g=arr[0]
for i in arr:
    g=gcd(g,i)
print(g==1)