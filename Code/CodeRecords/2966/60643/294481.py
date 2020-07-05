def clear_s(s,begin,end):
    for i in range(begin,end+1):
        s[i]=" "
    return s
def restore(n:int,s:list,t:list):
    sto=[]
    i=0
    while i<n:
        temp=[]
        dif=0
        cur=s[i]
        if cur not in t:
            return []
        p=t.index(cur)#从s开头开始遍历，在t中找相应元素的index 找到之后将t中目标元素置为“ ”
        temp.append(p)#2 1 1 1 1
                      #1 1 1 1 2
        for j in range(n-i):
            if p+j==n-1:#遍历到了t的最后
                dif = j
                break
            if s[i+j]==t[p+j]:#s,t同时向后走
                if j==n-i-1:#s走到了最后
                    dif=j
                continue
            else:
                dif=j-1#[i,i+diff]包含首尾 的区间内的字符是相同的
                break
        temp.append(p+dif)
        sto.append(temp)
        s=clear_s(s,i,i+dif)
        i=i+dif+1
    return sto


def jusgeAndFormat(lst:list):#lst中的值都是下标 所以要+1 并且长度不足3的都要重新格式化
    res=[]
    if len(lst)>3:
        res.append("NO")
    elif len(lst)==1:
        beg=lst[0][0]
        end=lst[0][1]
        if end-beg+1<3:
            res.append("NO")
    elif len(lst)==2:
        if lst[0][0]==lst[0][1] and lst[1][0]==lst[1][1]:
            res.append("NO")
        else:
            res.append("YES")
            for item in lst:
                if item[0]!=item[1]:
                    res.append(str(item[0]+1)+" "+str(item[0]+1))
                    res.append(str(item[0]+1+1)+" "+str(item[1]+1))
                else:
                    res.append(str(item[0]+1)+" "+str(item[1]+1))
    else:
        res.append("YES")
        for item in lst:
            begin=item[0]+1
            end=item[1]+1
            res.append(str(begin)+" "+str(end))
    return res


if __name__=="__main__":
    case=int(input())
    for _ in range(case):
        n,m=input().split()
        n=int(n)
        m=int(m)
        s=input().split()
        t=input().split()
        temp=restore(n,s,t)
        if len(temp)==0:
            print("NO")
        else:
            ans=jusgeAndFormat(temp)
            for i in ans:
                print(i)