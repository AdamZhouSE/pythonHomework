n=int(input())

#print(n)

i=0
while i<n:
    j=int(input())
    if(j%3==0):
        print(int(j/3-1),end=" ")
        print(int(j/3),end=" ")
        print(int(j/3+1))
    else:
        print(-1)
    i=i+1
