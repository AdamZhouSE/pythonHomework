def maxConnect(temp:int,index:int,n:int,lists:list)->int:
    lists.append(temp)
    add = 0;
    for a,b in conn:
        if a==temp and a not in lists and b not in lists:
            add += maxConnect(b,index,0,lists)
        if b==temp and a not in lists and b not in lists:
            add += maxConnect(a,index,0,lists)
    return add+1
def delete(index:int):
    for ele in conn:
        if ele[0]==index or ele[1]==index:
            k = maxConnect(ele[0] if ele[0]==index else ele[1],index,0,[index])
            subconn.append(k)
num = int(input())
conn = list()
for i in range(num-1):
    a,b = map(int,input().split())
    conn.append([a,b])
maxs = list()
for i in range(num):
    subconn = list()
    delete(i+1)
    maxs.append(max(subconn))
t = min(maxs)
for i in range(num):
    if maxs[i]==t:
        print("{}".format(i+1),end=' ')