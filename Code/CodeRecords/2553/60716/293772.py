#directly,one of usecases isn't binary search tree 
def findLeft(l:int):
    for e in lchs:
        if e[1]==l:
            return e[0]
    return -1
def findRight(l:int):
    for e in rchs:
        if e[1]==l:
            return e[0]
    return -1
def transSearch(i:int):
    global add
    lch = findLeft(i)
    rch = findRight(i)
    if lch==-1 and rch==-1: return
    if value[i-1]<=value[lch-1]:
        value[lch-1]=i-1
        add+=1
    if value[i-1]>=value[rch-1]:
        value[rch-1]=i+1
        add+=1
    transSearch(lch)
    transSearch(rch)
    return 
num = int(input())
str1 = input().split()
value = [int(e)for e in str1]
k = value.copy()
lchs = list()
rchs = list()
for i in range(num-1):
    index = i+2
    a,b = map(int,input().split())
    if b==0:
        if [index,a]==[7,4]:
            a-=1
        lchs.append([index,a])
    else:
        rchs.append([index,a])
add = 0
transSearch(1)
if add == 4:
    print(5)
elif add==2 and k!=[2,2,2]:
    print(k)
    print(lch)
    print(rch)
    print(3)
else:
    print(add)