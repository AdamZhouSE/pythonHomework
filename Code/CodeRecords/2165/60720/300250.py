import queue
size=int(input())
for k in range(size):
    q=queue.Queue()
    lst=[]
    list0=input().split()
    n=int(list0[0])
    s=list0[1]
    arr=[]
    isF=False
    input()
    for i in range(n):
        list0=input().split()
        if list0[0]==s and not isF:
            q.put(i)
            isF=True
        lst.append(list0[0])
        del list0[0]
        list1=[]
        for j in range(n):
            if list0[j]=='1':
                list1.append(j)
        arr.append(list1)
    visit=[0]*n
    road=[]
    while not q.empty():
        num=q.get()
        visit[num]=1
        road.append(lst[num])
        for i in range(len(arr[num])):
            if visit[arr[num][i]]==0:
                q.put(arr[num][i])
                visit[arr[num][i]]=1
    for i in range(len(road)-1):
        print(road[i],end=' ')
    print(road[-1])