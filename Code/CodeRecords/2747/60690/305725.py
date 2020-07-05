begin=input()
end=input()
wordlist=input()[2:-2].split("\",\"")
res=[]
def isSat(str1,str2):
    if len(str1)!=len(str2):return False
    count=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:count+=1
    if count==1:return True
    else:return False

def findAll(wordlist,l,res,begin,end):
    if begin==end:
        newList=l[:]
        res.append(newList)
        return
    for i in range(len(wordlist)):
        if isSat(begin,wordlist[i])==True and wordlist[i] not in l:
            l.append(wordlist[i])
            findAll(wordlist,l,res,wordlist[i],end)
    l.pop(-1)

l=[begin]
findAll(wordlist,l,res,begin,end)

if res==[]:print("[]")
else:
    minLen=len(res[0])
    for i in range(len(res)):
        if len(res[i])<minLen:
            minLen=len(res[i])
    print("[")
    for i in range(len(res)):
        if len(res[i]==minLen):
            print(res[i])
    print("]")