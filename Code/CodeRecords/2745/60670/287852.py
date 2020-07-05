def haveline(wordA,wordB):
    diff=0
    for i in range(0,len(wordA)):
        if wordA[i]!=wordB[i]:
            diff+=1
        if diff>=2:
            return False
    if diff==1:
        return True
    else:
        return False

def search(x,depth):
    if depth>beginNo:
        return
    global queue
    global mindepth
    global endNo
    global ans
    global visited
    queue.append(x)
    visited[x]=True
    if x==endNo:
        if depth<mindepth:
            ans=[]
            mindepth=depth
        ans.append(queue)
        visited[x]=False
        return
    global edge
    global n
    for i in range(0,n):
        if (edge[x][i]==1)and (not visited[i]):
            search(i,depth+1)
    visited[x]=False
    return

beginWord=input()
endWord=input()
wordList=eval(input())
n=len(wordList)
beginNo=0
endNo=0
if not beginWord in wordList:
    wordList.append(beginWord)
    beginNo=n
    n+=1
else :
    beginNo=wordList.index(beginWord)
if not endWord in wordList:
    wordList.append(endWord)
    endNo=n
    n+=1
else:
    endNo=wordList.index(endWord)
edge=[[0 for i in range(0,n)]for i in range(0,n)]
for i in range(0,n):
    for j in range(0,n):
        if haveline(wordList[i],wordList[j]):
            edge[i][j]=1
            edge[j][i]=1
visited=[False for i in range(0,n)]
finded=False
queue=[]
ans=[]
mindepth=n
search(beginNo,0)
print(ans)