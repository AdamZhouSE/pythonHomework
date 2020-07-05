a1=input()[1:-2].split(',')
a=[int(y) for y in a1]
target=int(input())
for j in range(len(a)):
    if a[j]==target:
        print(j)
    else:
        print(-1)
        
