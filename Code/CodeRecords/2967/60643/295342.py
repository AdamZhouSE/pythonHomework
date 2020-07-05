def find_common_substr(s1:str,s2:str):
    n=len(s1)
    p1=0
    st=set()
    record_pre=-1
    x=0
    while p1<len(s1):#ababc  #cbaab
        k = 0
        temp=""
        if p1!=record_pre:#pre用以解决p1进入新的目标字母时x还停留在p1前一个字符的查找Index的区间而未归0
            x=0
        if s1[p1] not in s2[x:]:#一定要是在x往后这个区间内没找到 不然下面的查找index会报错
            p1+=1
            continue
        else:
            p2=s2.index(s1[p1],x)
        while k<n-p1 and k<n-p2:
            if s1[p1+k]==s2[p2+k]:
                temp+=s1[p1+k]#or s2[p2+k]
                st.add(temp)
                k+=1
                continue
            else:
                #st.add(temp)
                x=p2+k
                k=0
                record_pre = p1#要记录一下 不然无法区分下面的p1是经过加一减一之后还等于原来的p1，还是没经过-1 直接加一等于下一个Index了
                p1-=1#用于抵消下面的p1+=1
                break
        p1+=1
    return st


if __name__=="__main__":
    n=int(input())
    strs=[]
    for _ in range(n):
        s=input()
        strs.append(s)
    c_s_of2=find_common_substr(strs[0],strs[1])
    res=list(c_s_of2)
    cpy=res
    if len(res)>2:
        lst=strs[2:]
        for i in cpy:
            for j in lst:
                if i not in j:
                    res.remove(i)
                    break#要加break 不然会导致已经删除的字符串被检验是否在接下来的 strs[x:]中
    lst = list(res)
    lst.sort(key=lambda x:len(x),reverse=True)
    print(len(lst[0]))