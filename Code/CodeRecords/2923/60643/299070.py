def solution(data,qry):
    dic={}#记录第x个数 被查询的次数
    for item in qry:
        l=item[0]
        r=item[1]
        for i in range(l,r+1):
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
    counter=sorted(dic.values(),reverse=True)
    data=sorted(data,reverse=True)
    sum=0
    for i in range(len(counter)):
        sum+=counter[i]*data[i]
    return sum


if __name__=="__main__":
    [n,q]=list(map(int,input().split()))
    data=list(map(int,input().split()))
    qry=[]
    for _ in range(q):
        [l,r]=list(map(int,input().split()))
        qry.append([l,r])
    ans=solution(data,qry)
    print(ans)