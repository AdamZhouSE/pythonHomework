n=int(input())
s=str(n)
lenl=len(s)
list1=list(s)
list1=[int(x) for x in list1]
list1.sort(reverse=True)
maxn=list1[0]
lst=['']*maxn
for i in range(lenl):
    sum=int(s[i])
    for j in range(maxn):
        if sum>0:
            lst[j]+='1'
            sum-=1
        elif len(lst[j])!=0:
            lst[j]+='0'
print(maxn)
for i in range(maxn-1):
    print(lst[i],end=' ')
print(lst[-1])
    