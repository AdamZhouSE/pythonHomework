n=int(input())
for w in range(n):
    yes=False
    res=[]
    N=int(input())
    string=input()
    try:
        array=list(map(int,string.split()))
    except:
        array=list(map(int,string.split(",")))
    sumPair={}
    for i in range(N-1):
        for j in range(i+1,N):
            su=array[i]+array[j]
            res.append([i+j,su,i,j])
    res.sort()
    for k in range(len(res)):
        if k==len(res)-1:
            print("no pairs")
        for t in range(k+1,len(res)):
            if res[k][1]==res[t][1]:
                print(str(res[k][2])+" "+str(res[k][3])+" "+str(res[t][2])+" "+str(res[t][3]))
                yes=True
                break
        if yes:
            break
            