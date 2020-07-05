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
            ans.clear()
            mindepth=depth
        if (depth==mindepth) and (not queue in ans):
            ans.append(queue.copy())
        visited[x]=False
        queue.pop()
        return
    global edge
    global n
    for i in range(0,n):
        if (edge[x][i]==1)and (not visited[i]):
            search(i,depth+1)
    visited[x]=False
    queue.pop()
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
queue=[]
ans=[]
mindepth=n
search(beginNo,0)
for i in range(0,len(ans)):
    for j in range(0,len(ans[i])):
        ans[i][j]=wordList[ans[i][j]]
if ans==[]:
    print(ans)
else:
    print('[')
    for i in range(0,len(ans)):
        print("  ",end='')
        print('["'+ans[i][0]+'"',end='')
        for j in range(1,len(ans[i])):
            print(',"'+ans[i][j]+'"',end='')
        print(']',end='')
        if i==len(ans)-1:
            print()
        else:
            print(',')
    print(']')