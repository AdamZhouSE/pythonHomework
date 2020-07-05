import re
pattern=re.compile(r"-?\d+")
a=input()
a=list(map(int,pattern.findall(a)))
nums=set(a)
longest_stack=0;
for num in nums:
    current_stack=0
    if(num-1 not in nums):
        current_num=num
        current_stack=1
        while(current_num+1 in nums):
            current_num+=1
            current_stack=current_stack+1
        longest_stack=max(longest_stack,current_stack)
print(longest_stack)