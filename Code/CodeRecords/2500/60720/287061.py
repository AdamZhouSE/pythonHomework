lst=eval(input())
result=[]
k=0
def fmax(j):
    maxn=0
    for k in range(0,j+1):
        maxn=max(maxn,lst[k])
    return maxn
def findex(num,j):
    for k in range(0,j+1):
        if num==lst[k]:
            return k
def rev(j):
    for k in range(0,j//2):
        tmp=lst[k]
        lst[k]=lst[j-k]
        lst[j-k]=tmp
for i in range(len(lst)-1):
    if fmax(len(lst)-1-i)!=lst[len(lst)-1-i]:
        k=findex(fmax(len(lst)-1-i),len(lst)-1-i)
        if k!=0:
            result.append(k+1)
            rev(k)
        rev(len(lst)-i-1)
        result.append(len(lst)-i)
print(result)