def dealRes():
    s=input()
    strs=s[1:-1].split(",")
    n=len(strs)
    count=0
    maxN=0
    while count<n-1:
        count2=count+1
        while count2<n:
            s=strs[count][1:-1]+strs[count2][1:-1]
            if judge(s):
                maxN=len(s) if len(s)>maxN else maxN
            count2+=1
        count+=1
    print(maxN)

def judge(s):
    index=0
    while index<len(s):
        if s.count(s[index])>1:
            return False
        else:
            index+=1
    return True
    

dealRes()