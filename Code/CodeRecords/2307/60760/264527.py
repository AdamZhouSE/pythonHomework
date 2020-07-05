numoflist=int(input())
2
lists=[]    #存输入的数组
3
for i in range(numoflist):
4
    size=input()
5
    lists.append(input().split(" "))
6
#lists.append("3 1 3 3 2".split(" "))
7
#lists.append("1 2 3")
8
results=[[] for i in range(numoflist)]  #存各个数组的多数元素
9
for i in range(numoflist):
10
    for j in lists[i]:
11
        if lists[i].count(j)>=len(lists[i])/2:
12
            results[i].append(j)
13
for i in range(numoflist):
14
    results[i]=set(results[i])
15
for i in results:
16
    if i==set():
17
        print(-1)
18
    else:
19
        for j in i:
20
            print(j,end="")
21
        print()numoflist=int(input())
lists=[]    #存输入的数组
for i in range(numoflist):
    size=input()
    lists.append(input().split(" "))
#lists.append("3 1 3 3 2".split(" "))
#lists.append("1 2 3")
print(lists)
results=[[] for i in range(numoflist)]  #存各个数组的多数元素
for i in range(numoflist):
    for j in lists[i]:
        if lists[i].count(j)>=len(lists[i])/2:
            results[i].append(j)
for i in range(numoflist):
    results[i]=set(results[i])
for i in results:
    if i==set():
        print(-1,end="")
    else:
        for j in i:
            print(j,end="")
        print()