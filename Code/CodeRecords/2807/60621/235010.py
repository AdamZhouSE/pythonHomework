ab=[int(x) for x in input().split()]
bb=[int(x) for x in input().split()]
cb=[int(x) for x in input().split()]
BOX,KEY=[0,0],[0,0]
def count(b,Box,Key,ch):
    coun=[]
    if ch=="b":
        coun=Box
    else:
        coun=Key
    for i in range(len(b)):
        coun[int(b[i]%2)]+=1
count(bb,BOX,KEY,"b")
count(cb,BOX,KEY,"k")
print(str(min(BOX[0],KEY[1])+min(BOX[1],KEY[0])))
