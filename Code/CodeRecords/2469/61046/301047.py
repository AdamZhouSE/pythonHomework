num=int(input())
leng=[]

for i in range(num):
    leng.append(input())

for i in range(num):
    ss=leng[i]
    test=leng[i]
    test=list(test)
    com = (set(sorted(test)))
    left=0
    right=len(com)-1
    res=[]
    while len(ss)-right>0:
        left = 0
        string=ss[left:right+1]
        string=set(string)
        while string!=com:
            if right<=len(ss)-1:
                right+=1
                string = ss[left:right + 1]
                string = set(string)
        while string==com:
            if left<=len(ss)-len(com):
                left+=1
                string = ss[left:right + 1]
                string = set(string)
        res.append(right-left+2)
        right+=1
    print(min(res))
