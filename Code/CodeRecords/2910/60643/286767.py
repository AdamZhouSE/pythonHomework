def solution(lst):
    pre=max(lst[0])
    for i in range(1,len(lst)):
        #pre>后面的矩形的长和宽
        if pre>=lst[i][0] and pre>=lst[i][1]:
            pre=max(lst[i])
        #只大于长宽中的一个
        elif pre>=min(lst[i]):
            pre=min(lst[i])
        else:
            return "NO"
    return "YES"


if __name__=="__main__":
    n=int(input())
    lst=[]
    for _ in range(n):
        temp=input().split()
        temp=[int(x) for x in temp]
        lst.append(temp)
    ans=solution(lst)
    print(ans)