testnum=int(input())
for i in range(testnum):
    string=input()
    anslist=[]
    count=1
    ans=0
    for j in range(len(string)):
        anslist.append(0)
    for j in range(len(string)):
        anslist[j]=1
        for m in range(j):
            if(ord(string[m])<ord(string[j])):
                anslist[j]=max(anslist[j],anslist[m]+1)
            ans = max(ans, anslist[j])

    print(ans)