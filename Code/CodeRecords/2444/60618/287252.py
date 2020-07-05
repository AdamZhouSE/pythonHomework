nums=list(input())
num=[]
for i in range(0,len(nums)):
    if nums[i].isdigit():
        num.append(int(nums[i]))
t=num[len(num)-1]
k=num[len(num)-2]
tnum=[]
knum=[]
del num[len(num)-1]
del num[len(num)-1]
if len(num)<k+1 or len(num)<=1:
    print("false")  
else:
    re=1
    for i in range(0,len(num)-k):
        for j in range(i,i+k+1):
            for l in range(j,i+k+1):
                if abs(num[l]-num[j])<=t:
                    
                    tnum.append(abs(num[l]-num[j]))
                    knum.append(l-j)
    if len(tnum)==0:
        print("false")
    elif max(tnum)!=t or max(knum)!=k:
        print("false")
    else:
        for i in range(0,len(tnum)):
            if tnum[i]==max(tnum) and knum[i]==k:
                print("true")
                
    
        
