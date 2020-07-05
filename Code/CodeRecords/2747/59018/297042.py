def check(s1,s2):
    diff=0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            if diff==1:
                return False
            else:
                diff+=1
    if diff==1:
        return True
    else:
        return False

def findPath(wordlist,path,end,res):
    if path[len(path)-1]==end:
        res.append(path)
        return
    for i in range(len(wordlist)):
        if wordlist[i] not in path and check(wordlist[i],path[len(path)-1]):
            findPath(wordlist,path+[wordlist[i]],end,res)
    return

w1=input()
w2=input()
wordlist=eval(input())
res=[]
findPath(wordlist,[w1],w2,res)
if res==[]:
    print(res)
else:
    mi=len(res[0])
    for i in range(len(res)):
        if mi>len(res[i]):
            mi=len(res[i])
    print("[")
    for i in range(len(res)):
        if len(res[i])==mi:
            print(res[i])
    print("]")