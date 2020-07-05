def partime_job():
    start=eval("["+input()+"]")
    end=eval("["+input()+"]")
    profit=eval("["+input()+"]")
    n=len(start)
    job=sorted(zip(end,start,profit))
    neigh_job=[-1]*n
    pro=[0]*(n+1)
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            if job[i][1]>=job[j][0]:
                neigh_job[i]=j
                break
    for i in range(0,n):
        pro[i+1]=max(pro[i],job[i][2]+pro[neigh_job[i]+1])
    print(pro[n])
    
if __name__=='__main__':
    partime_job()