a=int(input())
strs=[]
for i in range(a):
    strs.append(input())
for i in range(a):
    str=strs[i]
    l=len(strs[i])
    chs=[]
    for j in str:
        if(j not in chs):
            chs.append(j)
    tmp=[]
    i=0
    j=0
    minsize=l
    count=0
    while i<l:
        if str[i] not in tmp:
            tmp.append(str[i])
        if(len(chs)==len(tmp)):
            minsize=min(minsize,i-j+1)
            if(str[j] not in str[j+1:i+1]):
                tmp.remove(str[j])
            j=j+1
            i=i-1
        i=i+1
    print(minsize)

# 2
# aabcbcdbca
# aaab

