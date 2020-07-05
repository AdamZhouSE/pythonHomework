n=int(input())
list1=input().split()
list1=list(map(int,list1))
j=False
for i in range (0,n):
    if((i+1==list1[list1[list1[i]-1]-1]) ):
        j=True
        break
if(j):
    print("YES")
else:
    print("NO")
