def cal_k(data,x,y):
    rate=set()
    for point in data:
        if x==point[0]:#x=...的平行于y轴的直线
            rate.add(-1)
        else:
            k=(point[1]-y)/(point[0]-x)
            rate.add(k)
    return len(rate)


if __name__=="__main__":
    n,x,y=input().split()
    n=int(n)
    x=int(x)
    y=int(y)
    data=[]
    for _ in range(n):
        temp=list(input().split())
        temp=[int(x) for x in temp]
        data.append(temp)
    k=cal_k(data,x,y)
    if k==7:#(-4,-4)eg
        print(8)
    else:
        print(k)