def find(n):
    if n==1:
        return 0
    if n%2==0:
        return 1+find(n/2)
    if n%2!=0:
        return 1+min(find(n+1),find(n-1))

    
n=eval(input())
print(find(n))