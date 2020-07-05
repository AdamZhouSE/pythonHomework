def jobOrdering(starttime:[int],endtime:[int],profit:[int]):
    jobs=[[0,0,0] for _ in range(len(starttime))]
    for i in range(len(starttime)):
        jobs[i][0]=starttime[i]
        jobs[i][1]=endtime[i]
        jobs[i][2]=profit[i]
    jobs.sort()  # sort jobs by start time

    arr=[0 for _ in range(len(starttime))]
    res,tmp,maxpre=0,0,0
    for i in range(len(starttime)):
        for j in range(maxpre,i):
            if jobs[i][0]>=jobs[j][1]:
                if j==maxpre:
                    maxpre+=1
                tmp=max(tmp,arr[j])
        arr[i]=tmp+jobs[i][2]
        res=max(res,arr[i])

    return res

starttime=list(map(int,input().split(',')))
endtime=list(map(int,input().split(',')))
profit=list(map(int,input().split(',')))
print(jobOrdering(starttime,endtime,profit))