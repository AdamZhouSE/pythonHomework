n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
s=list1[0]
e=0
for i in range(n-1):
    e+=list1[i]-list1[i+1]
    if e<0:
        s=s-e
        e=0
print(s)        
    

