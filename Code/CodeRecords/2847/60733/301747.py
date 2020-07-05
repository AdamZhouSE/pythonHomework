n=input()
 
x=list(map(int,input().split()))
 
a,b=map(int,input().split())
 
print(sum(x[a-1:b-1:1]))