def find_kth(s,k):
    t=[]
    for i in range(k):
        t.append(s[i])
    t.sort(reverse=True)
    for j in range(k,len(s)):
        if s[j]<t[0]:
            t.pop(0)
            t.append(s[j])
            t.sort(reverse=True)
    return t[0]


def reverse_part(s,start,end):
    t=s[start:end+1]
    t.reverse()
    for i in range(len(t)):
        s[i+start]=t[i]       

a=int(input().strip())
s=[int(x) for x in input().strip().split()]
for i in range(a):
    index=s.index(find_kth(s,i+1))
    print(index+1,end=' ')
    if i<index:
        reverse_part(s,i,index)
    if i>index:
        reverse_part(s,index,i)
        