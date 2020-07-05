s=input()
if len(s)%2==1:
    print("-1")
else:
    ans,accumulation=0,0
    for i in s:
        if i=="2": accumulation+=1
        if i=="5": accumulation-=1
        if accumulation<0: 
            ans=-1
            break
        ans=max(ans,accumulation)
    print(ans)