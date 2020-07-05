import collections
beginword=input()
endword=input()
wordList=eval(input())
dict=collections.defaultdict(list)
leng=len(beginword)
for word in wordList:
    for i in range(leng):
        match=word[:i]+"*"+word[i+1:]
        dict[match].append(word)
visited={beginword:1}
queue=collections.deque([(beginword,1)])
pres=collections.defaultdict(list)
while queue:
    cur,level=queue.popleft()
    for i in range(len(cur)):
        match=cur[:i]+"*"+cur[i+1:]
        for word in dict[match]:
            if word not in visited:
                visited[word]=level+1
                queue.append((word,level+1))
            if(visited[word]==level+1):
                pres[word].append(cur)
    if(endword in visited and level+1>visited[endword]):
        break
ans=[]
if endword in visited:
    res = [[endword]]
    while res[0][0] != beginword:
        res = [[word] + r for r in res for word in pres[r[0]]]
    print(res)
else:
    print("[]")




