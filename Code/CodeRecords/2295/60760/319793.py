def func(trees:list,begin:int,m:int,n:int):
    fathers1=[]
    fathers2=[]
    son1=m
    son2=n
    while fathers2.count(begin)==0 or fathers1.count(begin)==0:
        for i in trees:
            if i[1] == son1 or i[2] == son1:
                fathers1.append(i[0])
                break
                son1 = i[0]
            if i[1] == son2 or i[2] == son2:
                fathers2.append(i[0])
                son2 = i[0]
                break
    for i in fathers1:
        if fathers2.count(i) > 0:
            return i

if __name__ == '__main__':
    temp = list(map(int, input().split(" ")))
    n = temp[0]  # 节点树
    begin = temp[1]
    trees = []
    for i in range(n):
        trees.append(list(map(int, input().split(" "))))
    target=list(map(int, input().split(" ")))
    print(func(trees,begin,target[0],target[1]))