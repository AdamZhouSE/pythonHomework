nums=input();
target=input();
a=0;
for i in range(0,len(nums)):
    if nums[i]==target:
        print(i);
        a=1;
        break;
if a==0:
    print("-1");
