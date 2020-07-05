num_=int(input())
for i in range(num_):
    N=int(input())
    nums=list(map(int,input().split(" ")))
    K=int(input())
    dui=[]
    for m in range(len(nums)):
        for n in range(i+1,len(nums)):
            if nums[m]+nums[n]==K and nums[m]!=nums[n]:
                if [nums[m],nums[n]] not in dui:
                    if [nums[n],nums[m]] not in dui:
                        dui.append([nums[m],nums[n]])
    if len(dui)==0:
        print(-1)
    else:
        for m in dui:
            print(str(m[0])+" "+str(m[1])+" "+str(K))
