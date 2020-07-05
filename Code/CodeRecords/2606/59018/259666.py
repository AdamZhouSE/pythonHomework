a1=input()[1:-2].split(',')
a=[int(y) for y in a1]
target=int(input())
flag=0
for j in range(len(a)):
    if a[j]==target:
        print(j)
        flag=1
if flag==0:
    print(-1)
        
