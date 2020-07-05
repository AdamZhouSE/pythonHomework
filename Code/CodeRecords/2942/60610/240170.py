num=input();
string=input();
nums=string.split();
nums.sort(key=None,reverse=True);
string="".join(nums);

print(string,end='');
