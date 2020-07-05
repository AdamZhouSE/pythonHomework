import bisect
def solution(jobs):#单个兼职的收入算作profit，多个被选中的收入算作income，end_income是选中的兼职的结束时间列表
    incomes=[0]#每个值都是累计薪酬，eg.index=1的是包含了一个工作的薪酬，index=2的数是两个工作的薪酬总和，对应的incomes_end数组里面：index=1是fistjob的profit,index=2是scnjob的profit
    incomes_ends=[0]
    for job in jobs:
        if job[0]>job[1]:#[(5, 1, 14), (3, 4, 11), (3, 5, 40), (4, 6, 70)]#expected81 but95有start>end的输入
            continue
        p=bisect.bisect_right(incomes_ends,job[0])#job[0]为该份兼职的开始时间，要求它比选中的兼职的结束时间晚，,且由于之前补了0，p一定>=1
        # 返回的是如果选中了它，它的开始时间在已经选中的incomes里面将会被安放的position,即它会作为第几份被pick up的job
        prev_end=p-1
        prev_income=incomes[prev_end]
        doi_income=prev_income+job[2]
        if doi_income<=incomes[-1]:
            continue
        incomes_ends.append(job[1])
        incomes.append(doi_income)
    return incomes[-1]

if __name__=="__main__":
    beg=list(map(int,input().split(",")))
    end=list(map(int,input().split(",")))
    profit = list(map(int, input().split(",")))
    jobs=sorted(zip(beg,end,profit),key=lambda x:x[1])
    ans=solution(jobs)
    print(ans)