nums=eval(input());
MAX=max(nums);
nums.remove(MAX);
nums=sorted(nums);
nums.insert(1,MAX);
print(nums);