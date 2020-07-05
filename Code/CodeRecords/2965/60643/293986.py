#区间的尾部元素不包含在内
def copyAndInsert(s:str,ops:list,m:int,k:int):
    for op in ops:
        sli=s[op[0]:op[1]]
        s=s[0:op[2]]+sli+s[op[2]:]
        if len(s)>m:
            s=s[:m]
    return s[:k]

if __name__=="__main__":
    k,m=input().split()
    k=int(k)
    m=int(m)
    s=input()
    n=int(input())
    ops=[]
    for _ in range(n):
        op=input().split()
        op=[int(x) for x in op]
        ops.append(op)
    res=copyAndInsert(s,ops,m,k)
    print(res,end="")