input=input();
nums=input.split("+");
nums.sort();
result="";
for i in nums:
    result=result+i+"+";
res=result[:len(result)-1]
print(res);