def isAlive(lst):
    res1="DEAD"
    res2="DEAD"
    suc_1=sum(item[1] for item in lst if item[0]==1)
    fai_1=sum(item[2] for item in lst if item[0]==1)
    if suc_1>=fai_1:
        res1="LIVE"
    suc_2 = sum(item[1] for item in lst if item[0] == 2)
    fai_2 = sum(item[2] for item in lst if item[0] == 2)
    if suc_2 >= fai_2:
        res2 = "LIVE"
    return res1,res2

if __name__=="__main__":
    n=int(input())
    lst=[]
    for i in range(n):
        data=input().split()
        data=[int(x) for x in data]
        lst.append(data)
    ans1,ans2=isAlive(lst)
    print(ans1)
    print(ans2)