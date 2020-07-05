num=int(input())
for i in range(num):
    s=input()
    l=[]
    for j in range(len(s)):
        l.append(s[j])
    n1=len(l)
    l=list(set(l))
    n2=len(l)
    print(n1-n2)