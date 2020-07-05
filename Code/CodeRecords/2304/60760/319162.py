def func1(trees:list,begin:int):
    fathers=[begin]
    sons=[]
    height=1
    visited=1
    res=[[begin]]
    while visited<len(trees):
        for i in fathers:
            for j in trees:
                if j[0]==i:
                    if j[1]!=0:
                        sons.append(j[1])
                        visited+=1
                    if j[2]!=0:
                        sons.append(j[2])
                        visited+=1
        print("Level "+str(height)+" :",end="")
        for k in fathers:
            print(" "+str(k),end="")
        print()
        fathers=list(sons)
        sons.clear()
        height+=1
    print("Level " + str(height) + " :", end="")
    for k in fathers:
        print(" " + str(k), end="")
    print()
def func2(trees:list,begin:int):
    fathers = [begin]
    sons = []
    res = [[begin]]
    visited = 1
    while visited < len(trees):
        for i in fathers:
            for j in trees:
                if j[0] == i:
                    if j[1] != 0:
                        sons.append(j[1])
                        visited+=1
                    if j[2] != 0:
                        sons.append(j[2])
                        visited+=1
        temp=list(sons)
        res.append(temp)
        fathers=list(sons)
        sons.clear()
    for i in range(len(res)):
        if i%2==0:
            print("Level "+str(i+1)+" from left to right:",end="")
            for j in res[i]:
                print(" "+str(j),end="")
            print()
        else:
            print("Level " + str(i + 1) + " from right to left:", end="")
            for j in res[i][::-1]:
                print(" " + str(j),end="")
            print()

temp=list(map(int,input().split(" ")))
n=temp[0]#节点树
begin=temp[1]
trees=[]
for i in range(n):
    trees.append(list(map(int,input().split(" "))))
func1(trees,begin)
func2(trees,begin)