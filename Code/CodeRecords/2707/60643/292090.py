def findAnother(n):
    if n%2==0:
        return n+1;
    return n-1


def findSwapTimes(lst:list):
    cnt=0
    for i in range(0,len(lst),2):
        n=lst[i]
        another=findAnother(n)
        if lst[i+1]!=another:
            pos=lst.index(another)
            lst[i+1],lst[pos]=lst[pos],lst[i+1]
            cnt+=1
        else:
            continue
    return cnt


if __name__=="__main__":
    lst=eval(input())
    ans=findSwapTimes(lst)
    print(ans)