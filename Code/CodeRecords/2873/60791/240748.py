n,m =  [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
result =[]
for item in a:
    for anjian in b:
        if(item == anjian):
            result.append(item)
for i in range(len(result)):
    if(i != len(result)-1):
        print(result[i],end=" ")
    else:
        print(result[i])
        