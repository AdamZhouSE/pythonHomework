n=int(input());
dic={};
for i in range(n):
    num=input().split(" ");
    numlist=list(int(x) for x in num);
    tot=sum(numlist);
    dic[i]=tot;
ss=dict(sorted(dic.items(),key=lambda x:x[1],reverse=True));
keylist=list(ss.keys());
print(keylist.index(0)+1)