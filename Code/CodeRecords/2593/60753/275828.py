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
            for b in range(l-2):
                for c in range(l-1):
                    for d in range(l):
                        if nl[a]+nl[b]==nl[c]+nl[d]:
                            if len(res)==0:
                                res.append(a)
                                res.append(b)
                                res.append(c)
                                res.append(d)
                            else:
                                if min(nl[a],nl[b],nl[c],nl[d])<min(res):
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
                                if min(nl[a],nl[b],nl[c],nl[d])<min(res):
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
                                if min(nl[a],nl[b],nl[c],nl[d])<min(res):
                                    res.append(a)
                                    res.append(d)
                                    res.append(b)
                                    res.append(c)
        if len(res)==0:
            print("no pairs")
        else:
            output=""
            for k in range(3):
                output+=str(res[k])+" "
            output+=str(res[3])
            print(output)
                        