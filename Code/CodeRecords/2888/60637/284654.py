n,m=map(int,input().split(' '))
arr=input().strip().split(' ')
count1,count_neg1=0,0
for i in arr:
    if(i==1):
        count1+=1
    else:
        count_neg1+=1
for i in range(m):
    l,r=map(int,input().strip().split(' '))
    result=1
    range=l-r+1
    if(range%2!=0):
        result=0
    if(count1<range/2 or count_neg1<range/2):
        result=0
    print(result)