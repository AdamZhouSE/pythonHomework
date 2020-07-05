from collections import Counter
string=input()
maxLetter=int(input())
minSize=int(input())
maxSize=int(input())
result=[]

for i in range(0,len(string)):
    for j in range(i+1,len(string)+1):
        subset=string[i:j]
        if len(set(list(subset)))<=maxLetter and minSize<=len(subset)<=maxSize:
            result.append(subset)

sortList=Counter(result).most_common()
if len(sortList)>0:
    print(sortList[0][1])
else:
    print(0)
