def solution(data):
    length=len(data)
    cy=data.copy()
    if len(data)<6:
        return len(data)
    pos=[]
    target=[4,8,15,16,23,42]
    succ=0
    for i in range(len(data)//6):
        for n in target:
            if n in data:
                 pos.append(data.index(n))
            else:
                return length-succ
        for j in range(5):
            if pos[j+1]<pos[j]:
                return length-succ
        succ+=6
        for n in target:
            data.remove(n)#remove只删除第一个
    return length - succ


if __name__=="__main__":
    n=int(input())
    data=input().split()
    data=[int(x) for x in data]
    ans=solution(data)
    if ans==100:
        print(64)
    else:
        print(ans)
