m=int(input())
n = int(input())
res =0
while m<n:
    if n%2==0:
        n= n/2
        res = res + 1
    else:
        n = (n+1)/2
        res = res + 2
        
print(int(res+m-n))