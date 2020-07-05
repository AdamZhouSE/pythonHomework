import collections
def maxFreq(s: str, len_of_mod,mod):
    n = len(s)
    occ = collections.defaultdict(int)
    maxT = 0
    for i in range(n - len_of_mod + 1):
        cur = s[i: i + len_of_mod]
        exist = set(cur)
        if len(exist) <= len_of_mod:
            occ[cur] += 1
    for ky,val in occ.items():
        if ky==mod:
             res=[val,ky]#ky:str val:merge times
             return res
    return -1

def solution(module,s):
    sto=[]
    res=[]
    for i in module:
        tmp=maxFreq(s,len(i),i)
        if tmp==-1:
            continue
        else:
            sto.append(tmp)
    sto=sorted(sto,key=lambda x:x[0],reverse=True)
    maxTimes=sto[0][0]
    for i in sto:
        if i[0]==maxTimes:
            res.append(i)
        elif i[0]<maxTimes:
            break
    return res
if __name__=="__main__":
    n=eval(input())
    module=[]
    while n!=0:
        for _ in range(n):
            module.append(input())
        s=input()
        res=solution(module,s)
        if len(res)>1:
            print(res[0][0])
            for i in res:
                print(i[1])
        else:
            print(res[0][0])
            print(res[0][1])
        n=eval(input())