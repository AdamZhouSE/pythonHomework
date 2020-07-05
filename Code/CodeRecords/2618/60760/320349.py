tests=int(input()) #找规律
lists=[]
all=[]
all.append(tests)
for i in range(tests):
    a=int(input())
    all.append(a)
    temp=(list(map(int,input().split(' '))))
    all+=temp
res=all
print(res)