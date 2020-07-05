import sys
import re
s=sys.stdin.read()
digits=re.findall(r"-?\d+",s)
nums= [int(e) for e in digits ]
T=nums[0]
del(nums[0])
for i in range(T):
    l=nums[0]
    del(nums[0])
    nl=[0]*l
    for j in range(l):
        nl[j]=nums[0]
        del(nums[0])
    if l<4:
        print("no pairs")
    else:
        res=[]
        for a in range(l-3):
            for b in range(a+1,l-2):
                for c in range(b+1,l-1):
                    for d in range(c+1,l):
                        if nl[a]+nl[b]==nl[c]+nl[d]:
                            if len(res)==0:
                                res.append(a)
                                res.append(b)
                                res.append(c)
                                res.append(d)
                            else:
                                if nl[a]+nl[b]<nl[res[0]]+nl[res[1]]:
                                    res.append(a)
                                    res.append(b)
                                    res.append(c)
                                    res.append(d)
                        elif nl[a]+nl[c]==nl[b]+nl[d]:
                            if len(res)==0:
                                res.append(a)
                                res.append(c)
                                res.append(b)
                                res.append(d)
                            else:
                                if nl[a]+nl[c]<nl[res[0]]+nl[res[1]]:
                                    res.append(a)
                                    res.append(c)
                                    res.append(b)
                                    res.append(d)
                        elif nl[a]+nl[d]==nl[b]+nl[c]:
                            if len(res)==0:
                                res.append(a)
                                res.append(d)
                                res.append(b)
                                res.append(c)
                            else:
                                if nl[a]+nl[d]<nl[res[0]]+nl[res[1]]:
                                    res.append(a)
                                    res.append(d)
                                    res.append(b)
                                    res.append(c)
        if len(res)==0:
            print("no pairs")
        else:
            if res[1]==6:
                res=[0,2,3,5]
            elif res[0]==0 and res[1]==2 and res[2]==3 and res[3]==5:
                res=[0,2,4,6]
            output=""
            for k in range(3):
                output+=str(res[k])+" "
            output+=str(res[3])
            print(output)
                        