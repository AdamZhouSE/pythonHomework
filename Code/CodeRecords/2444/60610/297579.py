string=input().split(", ");
nums=eval(string[0].split(" = ")[1]);
k=string[1].split(" = ")[1];
t=string[2].split(" = ")[1];
tar=0;
for i in range(len(nums)):
    for j in range(len(nums)):
        if(i!=j):
            if((abs(nums[i]-nums[j])<=int(t))&(abs(i-j) <= int(k))):
                tar=1;
                break;
if(tar==1):
    print("true");
else:
    print("false")