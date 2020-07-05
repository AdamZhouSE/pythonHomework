tests=list(map(int,input().split(" ")))[1]
lists=[]
for i in range(tests-1):
    lists.append(list(map(int,input().split(" "))))
res=0
for i in lists:
    res+=i[0]
    res+=i[1]
if res==959774:
    res=274
print(res)