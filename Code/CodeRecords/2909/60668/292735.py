import collections


def Strings_18_maxson(strings,maxLetters,minSize,maxSize):
    n = len(strings)
    oc = collections.defaultdict(int)
    ans = 0
    for i in range(n):
        exist = set()
        cu = ""
        for j in range(i,min(n,i+maxSize)):
            exist.add(strings[j])
            if len(exist)>maxLetters:
                break
            cu +=strings[j]
            if j-i+1>=minSize:
                oc[cu]+=1
                ans = max(ans,oc[cu])
    print(ans,end='\n')
if __name__=='__main__':
    strings = input()
    maxLetters = input()
    minSize = input()
    maxSize = input()
    Strings_18_maxson(strings,int(maxLetters),int(minSize),int(maxSize))