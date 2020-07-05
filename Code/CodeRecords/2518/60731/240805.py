l=input().split('],[')
str1=l[0]
str2=l[1]
house=list(map(int,str1[1:].split(',')))
hot=list(map(int,str2[:len(str2)-1].split(',')))
minPath=[]
for i in range(len(house)):
    path=[]
    for j in range(len(hot)):
        path.append(abs(house[i]-hot[j]))
    minPath.append(min(path))
res=max(minPath)
print(res)