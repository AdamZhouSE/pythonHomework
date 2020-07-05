def quick_sort(s,start,end):
    if end-start<=1:
        return
    standard=s[start]
    p=start
    q=end-1
    flag=True
    while True:
        if p==q:
            break
        if flag:
            if s[q]<standard:
                temp=s[p]
                s[p]=s[q]
                s[q]=temp
                te=p
                p=q
                q=te
                flag=False
                q+=1
            else:
                q-=1
        else:
            if s[q]>standard:
                temp=s[p]
                s[p]=s[q]
                s[q]=temp
                te = p
                p = q
                q = te
                flag=True
                q-=1
            else:
                q+=1
    quick_sort(s,0,p)
    quick_sort(s,p+1,end)
s=eval(input())
quick_sort(s,0,len(s))
print(s)