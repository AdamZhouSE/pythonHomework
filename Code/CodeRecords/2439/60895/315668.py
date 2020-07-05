from operator import xor

num_list = input().split(" ")
count=int(num_list[0])
tree=[[] for x in range(0,count+1)]
for i in range(0,count-1):
    num_list = list(map(int,input().split(" ")))
    tree[num_list[0]]=num_list[1:]
times=int(input())
for i in range(0,times):
    flag=1
    num_list = list(map(int,input().split(" ")))
    qidian=num_list[0]
    zhongdian=num_list[1]
    res = 0
    for j in range(0,count-1):
        next=tree[qidian][0]
        res = xor(res, tree[qidian][1])
        if next==zhongdian:
            flag=0
            break
        if tree[next]==[]:
            break
        qidian=next
    if flag:
        print(0)
    else:
        print(res)