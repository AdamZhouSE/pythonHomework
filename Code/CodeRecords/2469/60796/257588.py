T=int(input())
result=[]
while T>0:
    ls=input()
    this=10000
    for i in range(len(ls)):
        j=i
        while j<len(ls):
            subs=ls[i:j+1]
            can=1
            for n in range(len(ls)):
                if not subs.__contains__(ls[n]):
                    can=0
            if can==1:
                if len(subs)<this:
                    this=len(subs)
            j=j+1
    result.append(this)
    T=T-1
for i in range(len(result)):
    print(result[i])
