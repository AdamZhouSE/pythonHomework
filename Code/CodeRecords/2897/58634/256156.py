#set()的用法
def hasIntersection(a,b):
    intersection = list(set(a).intersection(set(b)))
    if intersection == []:
        return False
    else:
        return True

words = eval(input())
maxNum = 0
for i in range(len(words)-1):
    for j in range(i+1,len(words)):
        if hasIntersection(words[i],words[j]):
            continue
        else:
            maxNum = max(maxNum,len(words[i])*len(words[j]))
print(maxNum)