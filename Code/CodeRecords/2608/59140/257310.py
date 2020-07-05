def sub(s,i,res,result):  # 求全部子序列
    if i==len(s):
        if res!='':result.append(res)
    else:
        sub(s,i+1,res,result)
        sub(s, i + 1, res+s[i], result)
T=int(input())
for i in range(0,T):
    suborder=[]
    sub(input(),0,'',suborder)
    suborder=sorted(list(set(suborder)))
    result=suborder.copy()
    for x in suborder:
        if "aeiou".find(x[0])==-1:
            result.remove(x)
        elif "aeiou".find(x[len(x)-1])!=-1:
            result.remove(x)
    if len(result)!=0:print(" ".join(result))
    else:print(-1)