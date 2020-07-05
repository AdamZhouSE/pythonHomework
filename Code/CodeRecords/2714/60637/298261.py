import sys
words=sys.stdin.readlines()
words[-1]+='\n'
numOfWord = len(words)
for i in range(numOfWord):
    words[i]=words[i][:-1]
words.sort(key=lambda x:len(x))
ans = [-1] * numOfWord
max_route=[]
def include(str1,str2):
    str1=list(str1)
    str2=list(str2)
    for i in str1:
        if(i not in str2):
            return False
        del str2[str2.index(i)]
    return True
def sequence(i,route):
    global words,ans,numOfWord,max_route
    judge=False
    for j in range(i+1,numOfWord):
        if(include(words[i],words[j])and len(words[j])==len(words[i])+1):
            judge=True
            route.append(words[j])
            dp=1+sequence(j,list.copy(route))
            route=route[:-1]
            if(dp>ans[i]):
                ans[i]=dp
    if(not judge):
        if(len(route)>len(max_route)):
            max_route=route
        ans[i]=1

    return ans[i]
for i in range(numOfWord):
    if(ans[i]==-1):
        sequence(i,[words[i]])
print(max(ans))
for i in max_route:
    print(i)