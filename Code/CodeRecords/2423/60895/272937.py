t=int(input())
while t>0:
    t=t-1 
    n1,n2=input().split(' ')
    n1=int(n1)
    n2=int(n2)
    s1=input().split(' ')
    s2=input().split(' ')
    result='No'
    for i in range(0,n1-1):
        for j in range(i+1,n1):
            if int(s1[i])>int(s1[j]):
                s1[i],s1[j]=s1[j],s1[i]
    for p in range(0,n2-1):
        for q in range(p+1,n2):
            if int(s2[p])>int(s2[q]):
                s2[p],s2[q]=s2[q],s2[p]
    num=0
    for m in range(0,n2):
        for n in range(0,n1):
            if s2[m]==s1[n]:
                num=num+1
                break
    if num==n2:
        result='Yes'
    print(result)