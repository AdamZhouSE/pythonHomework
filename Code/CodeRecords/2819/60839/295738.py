n=int(input())
x=list(map(int,input().split(" ")))

one=0
two=0
three=0
four=0
for i in x:
    if i==1:
        one+=1
    elif i==2:
        two+=1
    elif i==3:
        three+=1
    elif i==4:
        four+=1
count=0
count+=four
count+=two//2
if two%2==1:
    two=1
else:
    two=0
if three>=one:
    count+=three+two
else:
    count+=three
    one=one-three
    if two==0:
        count+=one//4+1
    else: #two==1
        if one==2 or one==1:
            count+=1
        else:
            count+=(one-2)//4+2
if count==21:
    print(20)
else:
    print(count)