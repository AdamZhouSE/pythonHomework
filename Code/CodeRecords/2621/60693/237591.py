numbers=list(map(int,input().split(',')))
def max_sum_rec(nums,left,right):
    if left==right:
        if nums[left]>0:
            return nums[left]
        else:return 0
    center=int((left+right)/2)
    max_left_sum=max_sum_rec(nums,left,center)
    max_right_sum=max_sum_rec(nums,center+1,right)
    max_lb_sum=0
    lbsum=0
    for i in range(center,left-1,-1):
        lbsum+=nums[i]
        if lbsum>max_lb_sum:
            max_lb_sum=lbsum
    max_rb_sum=0
    rbsum=0
    for i in range(center+1,right+1):
        rbsum+=nums[i]
        if rbsum>max_rb_sum:
            max_rb_sum=rbsum
    return max(max(max_left_sum,max_right_sum),max_rb_sum+max_lb_sum)

print(max_sum_rec(numbers,0,len(numbers)-1))