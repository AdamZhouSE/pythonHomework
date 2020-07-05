def solution(data):
    temp=list(reversed(data))#这里一定要加list
    res=[]
    for i in temp:
        if i not in res:
            res.append(i)
    res=list(reversed(res))#这里也是
    return res

if __name__=="__main__":
    n=int(input())
    data = input().split()
    ans = solution(data)
    print(len(ans))
    print(" ".join(ans))