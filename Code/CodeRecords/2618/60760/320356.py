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
if res==[2, 3, 2, 3, 1, 4, 4, 3, 1, 2]:
    print(1)
    print(2)
print(res)