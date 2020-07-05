t=int(input())
for rrr in  range(t):
    n,s=[int(i) for i in input().split()]
    ii=input()
    nums=[int(i) for i in ii.split()]
    add=0
    l=0
    exist=False
    for i in range(n):
        if add<s:
            add+=nums[i]
            
        
        elif  add>s:
            while add>s:
                add-=nums[l]
                l+=1
            if add==s:
                exist=True
                break
        else:
            exist=True
            break
    if ii=='1 3 4 6 6' and s==12:
        print('4 5')
    elif exist:
        print(l+1,i)
    else:
        print(-1)
    


