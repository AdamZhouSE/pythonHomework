test=[]
for i in range(5):
    test.append(input().split(" "))
for i in range(5):
    for j in range(5):
        if test[i][j]=="1":
            r=i
            c=j
            break

print(abs(2-c)+abs(2-r))
