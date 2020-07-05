def findLeft(l:int):
    for e in lchs:
        if e[1]==i:
            return e[0]
    return -1
def findRight(l:int):
    for e in rchs:
        if e[1]==i:
            return e[0]
    return -1
def transSearch(i:int):
    lch = findLeft(i)
    rch = findRight(i)
    if lch==-1 and rch==-1: return
    if value[i-1]<=value[lch-1]:
        value[lch-1]=i-1
        add+=1
    if value[i-1]>=value[rch-1]:
        value[lch-1]=i+1
        add+=1
    transSearch(lch)
    transSearch(rch)
    return 
num = int(input())
str1 = input().split()
value = [int(e)for e in str1]
lchs = list()
rchs = list()
for i in range(num-1):
    index = i+2
    a,b = map(int,input().split())
    if b==0:
        lchs.append([index,a])
    else:
        rchs.append([index,a])
add = 0
transSearch(1)
print(add)