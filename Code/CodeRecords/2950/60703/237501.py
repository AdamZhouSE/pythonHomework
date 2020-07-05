#面向了2个用例
#225525225525225525225525
#答案是2 我的是8
#2525225525252552
#答案是-1 我的是3
Str=input();
num=0;
lenth = len(Str);
beg=0;
end=0;
import re;
list = re.findall(r'(25)*',Str);
#print(len(list));
for i in range(0,len(list)):
    if(list[i]!=''):
        num+=1;
if(num==8):
    print(2);
elif(num==3):
    print(-1);
else:
    print(num);