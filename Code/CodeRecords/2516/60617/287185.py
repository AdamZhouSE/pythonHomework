def interval():
    m=int(input())
    arr=[]
    for i in range(0,m):
        arr.append(eval("["+input()+"]"))
    res=[-1]*m
    temp=[]
    for i in range(0,m):
        temp.append([arr[i][0],i])
    temp=sorted(temp, key= lambda x:x[0])
    for i in range(0,m):
        end=arr[i][1]
        if end>temp[len(temp)-1][0]:
            continue
        else:
            l=0
            r=len(temp)-1
            while l<r:
                mid=(l+r)//2
                if end>temp[mid][0]:
                    l=mid+1
                else:
                    r=mid
            res[i]=temp[l][1]
    print(res)

if __name__=='__main__':
    interval()