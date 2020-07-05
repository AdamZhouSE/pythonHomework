t=int(input())
for i in range(t):
    n = int(input())
    liststr=list(map(int, input().split()))
    listlist=[]
    for lindex in range(n):
        for rindex in range(lindex,n):
            listlist.append(liststr[lindex:rindex+1])
    res=0
    for element in listlist:
        if len(element)==len(set(element)):
            res+=len(element)
    print(res)