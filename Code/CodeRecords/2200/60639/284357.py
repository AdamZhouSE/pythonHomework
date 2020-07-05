string=input()
standard=input()
standard=[i for i in standard]
goodList=[]
k=int(input())
for i in range(len(string)):
    for j in range(i,len(string)):
        if standard[i:j+1].count('0')<=k:
            goodList.append(string[i:j+1])
goodSet=set(goodList)
print(len(goodSet))