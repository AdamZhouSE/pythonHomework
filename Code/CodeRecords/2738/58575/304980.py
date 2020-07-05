head_end=input()
head_end=input()
res=[]
while head_end!="]":
    left=head_end.index("[")
    right=head_end.index("]")
    temp=head_end[left+1:right].split(",")
    i=0
    while i<len(temp):
        temp[i]=int(temp[i][1:-1])
        i+=1
    res.append(temp)
    head_end=input()
maxS=1
i=0
while i<len(res):
    j=0
    while j<len(res[i]):
        if res[i][j]==1:
            j_end=j+1
            while j_end<len(res[i]):
                if res[i][j_end]!=1:
                    break
                j_end+=1
            width=j_end-j
            i_end=i+1
            while i_end<len(res):
                judge=True
                t=j
                while t<j_end:
                    if res[i_end][t] != 1:
                        judge=False
                        break
                    t+=1
                if judge==False:
                    break
                i_end+=1
            heighth=i_end-i
            maxS=max(maxS,heighth*width)
        j+=1
    i+=1
print(maxS)