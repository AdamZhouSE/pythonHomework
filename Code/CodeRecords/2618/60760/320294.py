tests=int(input()) #找规律
lists=[]
all=[]
all.append(tests)
for i in range(tests):
    a=int(input())
    all.append(a)
    lists.append(list(map(int,input().split(' '))))
    all+=lists
res=sum(all)
print(res)