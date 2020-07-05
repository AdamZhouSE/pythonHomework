def ish(a):
    for i in range(0,int(len(a)/2)):
        if(a[i]!=a[(len(a)-1-i)]):
            return 0
    return 1
def find(a):
    flag=0
    step=0
    j=len(a)-1
    for i in range(0,len(a)):
        t=j
        while(a[i]!=a[t]):
            t-=1
        if(a[i]==a[t]):
            step+=(j-t)
            ch=str(a[t])
            for l in range(t,j):
                a=a[0:l]+a[(l+1)]+a[(l+1):len(a)]
            l = l + 1
            if(l==(len(a)-1)):
                a=a[0:(len(a)-1)]+ch
            else:
                a=a[0:l]+ch+a[(l+1):len(a)]
            j-=1
        if ish(a)==1:
            return step
    return step



num=int(input())
n=input()
re=[]
for i in range(26):
    re.append(0)
flag=0
for i in range(len(n)):
    for k in range(0,26):
        if(chr(ord('a')+k)==n[i]):
            re[k]+=1
            break
times=0
for i in range(26):
    if(re[i]%2!=0):
        for k in range(0,len(n)):
            if(chr(i+ord('a'))==n[k]):
                flag=k
        times+=1
    if(times>=2):
        print("Impossible")
        exit()
if ish(n)==1:
    print(0)
    exit()
print(find(n))