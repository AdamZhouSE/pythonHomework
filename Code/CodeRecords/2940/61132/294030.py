def min_subperiod_len(s,l,r):
    for i in range(1,(r-l+1)//2+1):
        if (r-l+1)%i==0:
            index = l
            while index+i<=r:
                if s[index]!=s[index+i]:
                    break
                index+=1
            else:
                return i
    else:
        return -1

def find_min_str(reco,res,s,l,r):
    if l>r:return -1
    if reco[l][r]!=-1:return reco[l][r]
    if l==r:
        res[l][l]=s[l]
        reco[l][l]=1
        return 1
    Min=r-l+2
    pos=l
    for i in range(l,r):
        tmp=find_min_str(reco,res,s,l,i)+find_min_str(reco,res,s,i+1,r)
        if Min>tmp:
            Min=tmp
            pos=i
        
    res[l][r]=res[l][pos]+res[pos+1][r]
    Len=min_subperiod_len(s,l,r)
    reco[l][r] = Min
    if Len==-1:
        return Min
    tmp=str((r-l+1)//Len)+'('+res[l][l+Len-1]+')'
    if len(tmp)<len(res[l][r]) :
        res[l][r]=tmp
        reco[l][r]=len(tmp)
        return len(tmp)
    return Min

s=list(input().split()[0])
min_len=[[-1 for i in range(len(s))]for i in range(len(s))]
res=[['' for i in range(len(s))]for i in range(len(s))]
find_min_str(min_len,res,s,0,len(s)-1)
print(res[0][len(s)-1])
#你这用例根本不是字典序最小