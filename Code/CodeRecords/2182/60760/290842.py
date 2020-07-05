def func(n:int,k:int):
    people=[i for i in range(1,n+1)]
    index=-1
    while people.count(-1)<n-1:
        i = 0
        while i< k:
            if people[(index+1)%n]!=-1:
                i=i+1
            index+=1
        people[index%n]=-1


    for i in people:
        if i!=-1:
            return i


tests=int(input())
lists=[]
for i in range(tests):
    lists.append(list(map(int,input().split(' '))))
for i in lists:
    print(func(i[0],i[1]))