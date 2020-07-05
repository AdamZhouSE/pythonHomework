a=eval(input())
dic={}
for num in a:
    if not(num in dic):
        dic[num]=1
    else:
        dic[num]+=1
l=sorted(dic.items(),key=lambda x:x[1],reverse=True)
m=len(a)//3
ll=[]
for k in l:
    if k[1]>m:
        ll.append(k[0])
print(ll)