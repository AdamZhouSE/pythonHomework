tests=list(map(int,input().split(" ")))[1]
lists=[]
for i in range(tests-1):
    lists.append(list(map(int,input().split(" "))))
res=0
for i in lists:
    res+=i[0]
    res+=i[1]
print(res)