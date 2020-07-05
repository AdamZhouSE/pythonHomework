group_num=1
arr=eval(input())
def isSameGroup(word1,word2):
    if(len(word1)!=len(word2)):
        return False
    if(sorted(word1)!=sorted(word2)):
        return False
    counter=0
    for c in word1:
        if(word2.index(c)!=word1.index(c)):
            counter+=1
    if(counter==2 or counter==0):
        return True
    else:
        return False
def belongTo(word,arr):
    for c in arr:
        if(isSameGroup(word,c)):
            return True
    return False

for i in range(1,len(arr)):
    if(not belongTo(arr[i],arr[0:i])):
        group_num+=1
print(group_num)