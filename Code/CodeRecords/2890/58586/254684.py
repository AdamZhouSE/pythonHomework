[n,x0,y0]=list(map(int,input().split(" ")))
def getK(pos1,pos2):
    if pos1[0]-pos2[0]==0:
        return 100000007
    else:
        return (pos1[1]-pos2[1])/(pos1[0]-pos2[0])
arr=[]
for i in range(n):
    pos=list(map(int,input().split(" ")))
    temp=getK(pos,[x0,y0])
    if temp not in arr:
        arr.append(temp)
print(len(arr))