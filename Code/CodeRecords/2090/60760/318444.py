tests=list(map(int,input().split(" ")))[0]
lists=[]
for i in range(tests-1):
    lists.append(list(map(int,input().split(" "))))
res=sum(lists)
print(res)
