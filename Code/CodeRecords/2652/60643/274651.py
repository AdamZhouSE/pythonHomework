from typing import List
def solution(data:List[List[int]], n:int, c:int, f:int):
    scores = [x[0] for x in data]
    money = [x[1] for x in data]
    for i in range(n//2,c-n//2):#可能作为中位数的数字的下标值
        # for j in range(-n//2,0+1):#也要能取到0 所以加+1
        left=money[i-n//2:i]
        right=money[-n//2+1:]
        temp_sum=sum(left)+sum(right)+money[i]
        if temp_sum<=f:
            return scores[i]
        else:
            continue
    return -1#找不到

if __name__=="__main__":
    lst=input().split()
    n=int(lst[0])
    c=int(lst[1])
    f=int(lst[2])
    data=[]
    for i in range(c):
        line=input().split()
        line=[int(x) for x in line]
        data.append(line)
    # print(data)
    middle_index=c//2+1
    data=sorted(data,key=lambda x:x[0],reverse=True)
    # print(ans)
    ans=solution(data,n,c,f)
    print(ans,end="")