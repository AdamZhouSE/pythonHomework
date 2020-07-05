a=int(input())
for i in range(0,a):
    b=input()
    result = []
    c=input().split(' ')
    count=1
    for j in range(0,len(c)):
        c[j]=int(c[j])
        count=count*c[j]
    for j in range(0,len(c)):
        print(int(count/c[j]),end=" ")
    print()