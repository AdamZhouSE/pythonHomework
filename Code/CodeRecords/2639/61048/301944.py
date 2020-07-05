def search8():
    s=input()
    k=int(input())
    res=0
    dic={}
    max_cnt=0
    for i in range(len(s)):
        dic[s[i]]=dic.get(s[i],0)+1
        max_cnt=max(max_cnt,dic[s[i]])
        if(res-max_cnt<k):
            res+=1
        else:
            dic[s[i-res]]-=1
    print(res)
    return

search8()