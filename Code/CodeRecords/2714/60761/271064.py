def ifainb(a,b):
    if a=="":
        return True
    elif(len(b)-len(a)!=1):
        return False
    for i in a:
        if i not in b:
            return False
    return True
def wordchain(preword,words):
    ans=[]
    if(len(words)==0):
        return preword
    if(words[0][0]!=len(preword[-1])+1 and preword[-1]!=""):
        return preword
    for word in words[0][1]:
        if(ifainb(preword[-1],word)):
            temp=wordchain(preword[:]+[word],words[1:])
            if(len(ans)<len(temp)):
                ans=temp
    if(len(preword)==1):
        temp=wordchain(preword[:],words[1:])
        if(len(ans)<len(temp)):
            ans=temp
    return ans
        
        
words=[]
try:
    while(True):
        word=input()
        length=len(word)
        if(not words):
            words.append([length,[word]])
        else:
            j=0
            for key in words:
                if key[0]==length:
                    key[1].append(word)
                    j=1
                    break
            if(j==0):
                words.append([length,[word]])
except:
    words.sort()
    wordchain=wordchain([""],words)
    wordchain.pop(0)
    print(len(wordchain))
    for word in wordchain:
        print(word)
    

           