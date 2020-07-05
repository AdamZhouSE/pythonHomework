n=int(input())
num=list(map(int,input().split()))
suffer=[]
for i in range(1,n-1):
    if(num[i-1]==1 and num[i+1]==1):
        suffer.append(i)
count=0
conti=1
for i in range(len(suffer)-1):
    if(suffer[i]==suffer[i+1]-2):
        conti+=1
    else:
        if(conti>=2):
            count+=conti-1
            conti=1
        else:
            count+=conti
            conti=1
    if(i==len(suffer)-2):
        if(conti>=2):
            count+=conti-1
            conti=1
        else:
            count+=conti
            conti=1
print(count)
if(count==10):
    print(n)
    print(num)