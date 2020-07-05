def func(nums,k):
    c=[]
    sum=0
    for num in nums:
        sum+=num
        c.append(sum)
    for i in range(len(c)):
        for j in range(i+1,len(c)):
            if (c[j]-c[i])%k==0: return True
    return False
lst="["+input()+"]"
if func(eval(lst),int(input())): print("True")
else: print("False")