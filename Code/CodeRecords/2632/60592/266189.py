tests = input().split()
n = int(tests[0])
com = int(tests[1])
rec=[]
hou = [0]*n
bug = []
for i in range(0,com):
    ls = input().split()
    bug.append(ls)
    mes = ls[0]
    if mes=='D':
        num = int(ls[1])-1
        rec.append(num)
        hou[num]=-1
    elif mes=='R' and len(rec)>0:
        num = rec[len(rec)-1]
        rec.pop()
        hou[num]=0
    elif mes=='Q':
        num = int(ls[1])-1
        if hou[num]==-1:
            print(0)
        else:
            res=1
            j = num+1
            while j<n and hou[j]!=-1:
                res+=1
                j+=1
            j = num-1
            while j>=0 and hou[j]!=-1:
                res+=1
                j-=1
            print(res)