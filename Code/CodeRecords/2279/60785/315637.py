t=int(input())
for rrr in  range(t):
    n,s=[int(i) for i in input().split()]
    nums=[int(i) for i in input().split()]
    add=0
    l=0
    for i in range(n):
        if add<s:
            add+=nums[i]
            
        
        if  add>s:
            while add>s:
                add-=nums[l]
                l+=1
            if add==s:
                break
    print(l,i,s,nums)


