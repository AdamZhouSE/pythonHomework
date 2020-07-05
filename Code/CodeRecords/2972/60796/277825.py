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
            if this!="Yes":
                this="Yes"
                #从后面开始看
                i=len(x)-1
                j=len(y)-1
                while i>=0:
                    if y[j]!=x[i]:
                        r=j
                        while y[j]!=x[i]:
                            j=j-1
                            if j==0:
                                this="No"
                                break
                        l=j+1
                        sub=y[j+1:r+1]
                        if sub[0]==y[j]:
                            this="No"
                        for k in range(len(sub)-1):
                            if sub[k]==sub[k-1]:
                                this="No"
                                break
                        i=i-1
                        j=j-1
                    else:
                        i=i-1
                        j=j-1
                    if j==0 or this=="No":
                        break

    result.append(this)
    N=N-1

for i in range(len(result)):
    print(result[i])