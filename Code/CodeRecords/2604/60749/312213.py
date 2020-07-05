s=input()
s=s[1:len(s)-1]
ans=s.split(", ")
ans2=[]
for h in ans:
    ans2.append(h[1])
target=input()
ans2=sorted(ans2)
if(ans2[-1]>target):
    if(ans2[0]>target):
        print(ans2[0])
    else:

        for h in range(0,len(ans2)-1):
            if(ans2[h]<=target and ans2[h+1]>target):
                index=h+1
                break
    
        print(ans2[index])
else:
    print(ans2[0])
    