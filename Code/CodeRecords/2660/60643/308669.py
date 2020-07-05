def solution(ops,res):
    s=[]
    i=0
    cnt=0
   # res=[]
    while i<len(ops):
        if ops[i][0]=="T":
            s.append(ops[i][1])
        elif ops[i][0]=="Q":
            res.append(s[ops[i][1]-1])
        if ops[i][0]=="U":
            x=ops[i][1]
            rec=i
            for j in range(i,-1,-1):
                if cnt==x:
                    rec=j+1
                    break
                else:
                    if ops[j][0]=="T":
                        cnt+=1
            ops=ops[:rec]+ops[i+1:]
            return solution(ops,res)
        i+=1
    return res

if __name__=="__main__":
    t=int(input())
    ops=[]
    for _ in range(t):
        tmp=input().split()
        if not tmp[1].isalpha():
            tmp[1]=int(tmp[1])
        ops.append(tmp)
    #ops=[['T', 'a'], ['T', 'b'], ['T', 'c'], ['T', 'd'], ['U', 1], ['Q', 3], ['T', 'c'], ['Q', 3]]
    res=solution(ops,[])
    for i in res:
        print(i)