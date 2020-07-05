import sys
n=(int)(input())
string=input()
temp1=[]
temp2=[]
def swap(i,j):
    global temp1
    t=temp1[i]
    temp1[i]=temp1[j]
    temp1[j]=t
for i in range(len(string)):
    if(string[i] not in temp1):
        temp1.append(string[i])
        temp2.append(1)
    else:
        temp2[temp1.index(string[i])]+=1
result=0
temp1=list(string)
judge=True
for i in temp2:
    if(i%2!=0):
        judge=False
        break
if((n%2==0 and not judge)or(n%2!=0 and judge)):
    print("Impossible")
    sys.exit()
else:
    r=n-1
    for i in range((int)(n/2)):
        for j in range(r,i,-1):
            if(temp1[j]==temp1[i]):
                for k in range(j,r):
                    swap(k,k+1)
                    result+=1
                r-=1
                break
print(result)

