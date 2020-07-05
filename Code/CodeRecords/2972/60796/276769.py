N=int(input())
result=[]
while N>0:
    this="Yes"
    x=input()
    y=input()
    if x==y:
        this="Yes"
    else:
        if len(x)==len(y)==1:
            this="No"
        else:
            #看x是不是y前面的连续子字符串
            for i in range(1,len(y)):
                t=y[:i]
                if x==t:
                    this="Yes"
                    break
            if this!="yes":
                i=0
                j=0
                while i<len(x):
                    if x[i]==y[j]:
                        i=i+1
                        j=j+1
                    else:
                        l=j
                        r=l+1
                        while r<len(y):
                            if i<len(x)-1 and y[r]==x[i]:
                                break
                            else:
                                r=r+1
                        sub=y[l:r]
                        if y[0]==x[i-1]:
                            this="No"
                        for k in range(len(sub)-1):
                            if sub[k]==sub[k+1]:
                                this="No"
                                break
                        if this=="No":
                            break
                        else:
                            i=i+1
                            j=r

    result.append(this)
    N=N-1

for i in range(len(result)):
    print(result[i])