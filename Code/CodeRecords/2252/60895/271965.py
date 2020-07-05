t=int(input())
while t>0:
    t=t-1
    s=list(input())
    c=list(input())
    num=0
    for i in range(0,len(c)-1):
        for j in range(i+1,len(c)):
            if ord(c[i])>ord(c[j]):
                c[i],c[j]=c[j],c[i]
    for m in range(0,len(s)-len(c)+1):
        temp=s[m:m+len(c)]
        for p in range(0,len(temp)-1):
            for q in range(p+1,len(temp)):
                if ord(temp[p])>ord(temp[q]):
                    temp[p],temp[q]=temp[q],temp[p]
        if c==temp:
            num=num+1
    print(num)