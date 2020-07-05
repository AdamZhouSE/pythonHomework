def solution(data):
    temp=[]
    max_len=0
    for i in data:
        if i not in temp:
            temp.append(i)
            max_len=max(len(temp),max_len)
        else:
            temp.remove(i)
    return max_len


if __name__=="__main__":
    n=int(input())
    data=input().split()
    data=[int(x) for x in data]
    ans=solution(data)
    print(ans)