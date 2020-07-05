import math
def change(n):
    count=1
    while n>1:
        n=n//2
        count=count+1
    a=[]
    for j in range((count+1)/2):
        a.append((math.pow(4,(j+1)/2)-1)/3)
    print(a)
        
        
         







T=int(input())
for i in range(T):
    n=int(input())
    print(n)
    change(n)