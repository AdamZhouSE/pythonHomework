num=int(input());
for i in range(num):
    length=int(input());
    string=input().split();
    result=0;
    while(string!=[]):
        nums=string[0];
        result=string.count(nums)//2*2+result;
        while(nums in string):
            string.remove(nums);
    print(result);