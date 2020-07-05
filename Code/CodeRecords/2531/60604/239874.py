a=list(input())
a.sort()
count=[]
let=[]
let.append(a[0])
count.append(1)
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        count[len(count)-1]+=1
    else:
        count.append(1)
        let.append(a[i])
for i in range(len(count)):
    for j in range(len(count)-1,i,-1):
        if count[j]>count[j-1]:
            tmp=count[j]
            count[j]=count[j-1]
            count[j-1]=tmp
            tmp=let[j]
            let[j]=let[j-1]
            let[j-1]=tmp
def pt(a,b):
    while(b>0):
        print(a,end="")
        b-=1
for i in range(len(count)):
    pt(let[i],count[i])
print()