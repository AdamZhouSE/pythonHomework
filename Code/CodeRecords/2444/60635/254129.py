src=input().split(', ')
nums=[]
k=t=0
def judge(k,t,l):
    for i in range(l-k):
        for j in range(i+1,i+k+1 if i+k<=l-1 else l):
            if abs(nums[i]-nums[j])<=t:
                return True
    return False
for expr in src:
    exec(expr)
if judge(k,t,len(nums)):
    print('true')
else:
    print('false')


    