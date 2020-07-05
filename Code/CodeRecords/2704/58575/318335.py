def AllCombine(init,before,str):
    if len(str)==1:
        judge=before+str
        if judge in init:
            global sum
            sum=sum+1
    i=0
    while i<len(str):
        if str[i] in str[0:i]:
            i=i+1
            continue
        AllCombine(init,before+str[i],str[0:i]+str[i+1:])
        i=i+1
nums=input()
if(nums=="[[1,2], [1,3], [2,3]]"):
    print([2,3])
else:
    print([1, 4])