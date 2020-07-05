def func(trees:list,n:int):
    sorted(trees)
    begin=trees[0][0]
    fathers = [begin]
    sons = []
    res = [[begin]]
    visited = 1
    height=1
    while visited < len(trees):
        for i in fathers:
            for j in trees:
                if j[0] == i:
                        sons.append(j[1])
                        visited += 1
        fathers = list(sons)
        sons.clear()
        height+=1
    return height
if __name__ == '__main__':

    n=int(input())
    trees=[]
    for i in range(n-1):
        trees.append(list(map(int,input().split(" "))))
    print(func(trees,n))