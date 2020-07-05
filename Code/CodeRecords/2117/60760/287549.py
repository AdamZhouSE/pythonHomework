n=int(input())
lights=[1]*n
for i in range(1,n):
    j=i
    while j<n:
        if lights[j]==1:
            lights[j]=0
        else:
            lights[j]=1

        j=j+i+1
print(lights.count(1))