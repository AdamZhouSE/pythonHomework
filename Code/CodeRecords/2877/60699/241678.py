input()
list1=list(map(int,input().split(' ')))
cnt=[]
cnt.append(list1[0])
for i in range(1,len(list1)):
    cnt.append(list1[i]+cnt[len(cnt)-1])
res=-10000000000
res=max(res,-cnt[len(cnt)-1])
for i in range(0,len(cnt)):
    res=max(res,cnt[i]-(cnt[len(cnt)-1]-cnt[i]))
print(res)