def inthat(a,string,time):
    have=False
    for i in range(len(string)):
        s=string[i]
        isin = True
        if len(s)==len(a):
            for j in range(len(a)):
                y=a[j]
                h=False
                for k in range(len(s)):
                    x=s[k]
                    if x==y:
                        h=True
                        break
                if not h:
                    isin=False
                    break
        else:
            isin=False
        if isin:
            have=True
            break
    if have:
        time[i]=time[i]+1
    else:
        string.append(a)
        time.append(1)
    return string,time
def bubble(time):
    for i in range(len(time)-1):
        j=0
        while j<len(time)-i-1:
            if time[j]>time[j+1]:
                time[j],time[j+1]=time[j+1],time[j]
            j=j+1
    return time

N=int(input())
result=[]
while N>0:
    n=int(input())
    ls=input().split(" ")
    string=[]
    time=[]
    for i in range(len(ls)):
        a=ls[i]
        r=inthat(a,string,time)
        string=r[0]
        time=r[1]
    this=""
    time=bubble(time)
    for i in range(len(time)-1):
        this=this+str(time[i])+" "
    this=this+str(time[len(time)-1])
    result.append(this)

    N=N-1

for i in range(len(result)):
    print(result[i])

