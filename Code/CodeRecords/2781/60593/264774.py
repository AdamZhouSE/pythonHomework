import sys
def insert(t):
    global tot
    p=1
    for i in range(len(t)):
        k=ord(t[i])-ord('0')
        summ[p]+=1
        if(not trie[p][k]):
            tot+=1
            trie[p][k]=tot
        p=trie[p][k]
    summ[p]+=1
    ennd[p]=1
def dfs(x):
    global ans
    if(ennd[x] and summ[x]>=2):
        ans=1
    if(trie[x][0]):
        dfs(trie[x][0])
    if(trie[x][1]):
        dfs(trie[x][1])
ls=sys.stdin.readlines()
cnt=0
l=0
while(l<len(list(ls))):
    cnt+=1
    line=ls[l].replace('\n','')
    if(line=='9'):
        l+=1
        continue
    ans,tot=0,1
    ennd,summ,trie=[False]*1000,[0]*1000,[[0]*2 for i in range(1000)]
    insert(line)
    while(True):
        l+=1
        if(ls[l].replace('\n','')=='9'):
            break
        insert(ls[l].replace('\n',''))
    dfs(1)
    if(ans):
        print('Set %o is not immediately decodable'%cnt)
    else:
        print('Set %o is immediately decodable'%cnt)

