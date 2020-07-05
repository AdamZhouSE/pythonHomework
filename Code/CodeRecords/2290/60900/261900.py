n = int(input())
test = []
for i in range (0,n):
    a = int(input())
    test.append(input().split(" "))

for i in range(0,n):
    for j in range(0,len(test[i])):
        test[i][j]=int(test[i][j])

for i in range(0,n):
    for j in range(0,len(test[i])-1):
        if test[i][j+1]<test[i][j]:
            test[i][j]=test[i][j+1]
        else:
            test[i][j]=-1

for i in range(0,n):
    for j in range(0,len(test[i])-1):
        print(test[i][j],end=' ')
    print("-1 ")