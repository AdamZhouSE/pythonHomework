
def recursion(degree,list,start,end,answer):
    if str(answer).__len__()==degree:
        answerlist.append(answer)
        return
    for i in range(start,end):
        answer+=str(list[i])
        recursion(degree,list,i+1,end,answer)
        answer=answer[:-1]
def sum(n):
    n=[int(x) for x in list(n)]
    answer=0
    for i in n:
        answer+=i
    return answer
times=int(input())
for i in range(times):
    answerlist=[]
    n=int(input())
    nums=input().split()
    nums=[int(x) for x in nums]
    sb=int(input())
    result=0
    for i in range(1, n+1):
        recursion(i, nums, 0, n, "")
    for i in answerlist:
        if sum(i)==sb:
            result+=1
    print(result)