def royal_lady():
    firstRow=input().split(" ")
    n=int(firstRow[0])
    k=int(firstRow[1])
    motherTree=[]
    nameStr=[]
    for i in range(0, n):
        motherTree.append(input().split(" "))
    for i in range(0, k):
        nameStr.append(input())
    nameLi=[]
    nameLi.append(motherTree[0][0])
    for i in range(1, n):
        name=motherTree[i][0]
        motherNum=int(motherTree[i][1])
        name=name+nameLi[motherNum-1]
        nameLi.append(name)
    for start in nameStr:
        num=0
        for name in nameLi:
            if name.startswith(start):
                num+=1
        print(num)
        
if __name__=='__main__':
    royal_lady()