numoflist=int(input())
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