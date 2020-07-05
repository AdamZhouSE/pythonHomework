def perm(lst,k,m,res):#k~m为要递归全排列的字符串范围 m一直不变为（len-1)
    i=0
    if k==m:
        res.append("".join(lst))
    else:
        for i in range(k,m+1):
            if isDuplicate(lst,k,i):
                continue
            swap(lst,k,i)
            perm(lst,k+1,m,res)
            swap(lst,k,i)


def swap(lst,i,j):
    temp=lst[i]
    lst[i]=lst[j]
    lst[j]=temp

def isDuplicate(lst,k,i):#看list[i]在位置k是不是已经出现过 即k~i-1位置是不是有字符和i位置的字符一样
    for pos in range(k,i):
        if lst[pos]==lst[i]:
            return True
    return False


if __name__=="__main__":
    s=input()
    n=int(input())
    strLst=[]
    cnt=0
    ans=[]
    while cnt<n:
        tempStr=input()
        strLst.append(tempStr)
        cnt+=1

    for str in strLst:#每个字符串
        temp=list(str)
        res=[]
        perm(temp,0,len(temp)-1,res) #recursive len=8
        for i in res:
            ans.append(i)
    times=0
    for i in ans:
        if i in s:
            times+=1
    print(times)