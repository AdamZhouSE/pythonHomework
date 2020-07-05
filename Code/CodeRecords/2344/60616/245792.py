def rotate(src,List):
    size=len(List)
    ans=[]
    for i in range(src,size):
        ans.append(int(List[i]))
    for i in range(src):
        ans.append(int(List[i]))
    return ans

testNum=int(input())
for i in range (testNum):
    size=int(input())
    rawInputs=input().split(' ')
    items=[]
    for rawInput in rawInputs:
        items.append(int(rawInput))
    d=int(input())
    res=rotate(d,items)
    print(" ".join(str(i) for i in res),'')