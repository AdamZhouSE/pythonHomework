s=input()
Q=int(input())
arr=[]
for i in range(0,Q):
    arr=arr+[input()]
for k in range(0,Q):
    if arr[k]=='3':
        r=0
        for i in range(1,len(s)+1):
            for j in range(0,len(s)-i+1):
                s1=s[j:j+i]
                p=True
                for m in range(0,int(len(s1)/2)):
                    if s1[m:m+1]!=s1[len(s1)-m-1:len(s1)-m]:
                        p=False
                        break
                if p:
                    r+=1
        print(r)
    elif arr[k][0:1]=='1':
        s=s+arr[k][2:]
    else:
        a2=list(arr[k][2:])
        a1=[]
        for i in range(0,len(a2)):
            a1=[a2[i]]+a1
        s2=''
        for i in range(0,len(a2)):
            s2=s2+a1[i]
        s=s2+s

