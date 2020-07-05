def getAppeartimes(target,string):
    cnt = 0
    for i in range(0,len(string)-len(target)+1):
        #print()
        if(string[i:i+len(target)]==target):
            cnt += 1
    return cnt

def getNumOfDifferentLetters(s):
    temp = set(s)
    return len(temp)


s = input()
#print("s is",s)
maxLetters = int(input())
minSize = int(input())
maxSize = int(input())
res = 0
for i in range(0,len(s)-minSize+1):
    target = s[i:i+minSize]
    #print("Tar is ",target)
    #print("Target is ",target)
    if(getNumOfDifferentLetters(target)<maxSize):
        temp = getAppeartimes(target,s)
        if(temp>res):
            res = temp
print(res)
