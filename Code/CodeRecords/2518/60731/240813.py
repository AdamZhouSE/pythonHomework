str1=input()
str2=input()
house=list(map(int,str1.split(',')))
hot=list(map(int,str2.split(',')))
minPath=[]
for i in range(len(house)):
    path=[]
    for j in range(len(hot)):
        path.append(abs(house[i]-hot[j]))
    minPath.append(min(path))
res=max(minPath)
print(res)