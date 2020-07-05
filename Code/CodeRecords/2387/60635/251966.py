info = input().split()
n = int(info[0])
m = int(info[1])
src = [int(x) for x in input().split()]
def local_sort(src,start,end,reverse):
    if not reverse:
        for i in range(start,end-1):
            minvalue = src[i]
            index=i
            for j in range(i+1,end):
                if src[j]<minvalue:
                    minvalue=src[j]
                    index=j
            src[i],src[index]=src[index],src[i]
    else:
        for i in range(start,end-1):
            maxvalue = src[i]
            index=i
            for j in range(i+1,end):
                if src[j]>maxvalue:
                    maxvalue=src[j]
                    index=j
            src[i],src[index]=src[index],src[i]
for i in range(m):
    request = [int(x) for x in input().split()]
    isreverse = request[0] == 1
    local_sort(src,request[1]-1,request[2],isreverse)
num=int(input())
print(src[num-1])
    