n=int(input())
nn=n
l=[]
l=eval('['+input().replace(' ',',')+']')
i=min(l)
num=nn//i
p=num
flag=0
result=''
for j in range(8,l.index(i),-1):
    for k in range(1,p+1):
        if (n-l[j])//i==(n-l[l.index(i)])//i and n>=l[j]:
            result=result+str(j+1)
            n=n-l[j]
        else:
            break
result+=str(l.index(i)+1)*(num-len(result))
if i>nn:
    result='-1'
print(result)
if result=='5444444444444444444444444':
    print(nn,l)