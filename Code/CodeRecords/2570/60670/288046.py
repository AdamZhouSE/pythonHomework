def search(x,depth):
    global envelops
    global num
    global n
    num=max(num,depth)
    for i in range(x+1,n):
        if envelops[i][0]>envelops[x][0] and envelops[i][1]>envelops[x][1]:
            search(i,depth+1)
    return

n=int(input())
envelops=[]
for i in range(0,n):
    envelops.append(list(map(int,input().split(','))))
envelops=sorted(envelops,key=lambda x:(x[0],x[1]))
num=0
for i in range(0,n):
    search(i,1)
print(num)