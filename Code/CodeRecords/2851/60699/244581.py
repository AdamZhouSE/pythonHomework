cnt=int(input())
res=0
for i in range(0,cnt):
    list1 = list(map(int, input().split(' ')))
    res=max(res,list1[0]+list1[1])
print(res)