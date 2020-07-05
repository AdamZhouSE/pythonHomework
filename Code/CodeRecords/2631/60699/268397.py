list1=list(map(int,input().split(' ')))
n=list1[0]
G=list1[1]
up=G
list1=[]
dict={}
for i in range(n):
    temp=input().split(' ')
    list1.append((int(temp[0]),int(temp[1]),int(temp[2])))
list1.sort()
res=0
for temp in list1:

    if temp[1] not in dict:
        prev=G
        cur=prev+temp[2]
        if prev==up and cur<up:
            res+=1
        elif prev<=up and cur == max(cur,up):
            res+=1
            up=max(cur,up)
        dict[temp[1]]=cur
    else:
        prev = dict[temp[1]]
        cur = prev + temp[2]
        if prev == up and cur < up:
            res += 1
        elif prev <= up and cur == max(cur, up):
            res += 1
            up = max(cur, up)
        dict[temp[1]] = cur
print(res)