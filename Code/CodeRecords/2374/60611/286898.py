import sys
number=int(input())
for i in range(number):
    l=[]
    l.append(int(input()))
    l.append(list(map(int,input().split(" "))))
    s=list(set(l[1]))
    s=sorted(s)
    assist=[]
    for j in s:
        assist.append(l[1].count(j))
    result=[]
    for j in range(len(s)):
        maximum=max(assist)
        position=assist.index(maximum)
        for k in range(maximum):
            result.append(s[position])
        assist[position]=-1
    for j in range(l[0]):
        print(result[j],end=" ")
    print()
      