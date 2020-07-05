import re;


firstr = input();
secstr = input();
# result=re.findall(r'' + strmy ,forstr)
#OK成功引入变量：：r''（一定要紧贴写！！） 确定是r字符串，，后面其实就是字符串拼接了！！！
# print(result)
result=0;
for lengh in range(1,len(firstr)+1):
    for l in range(len(firstr)):
        if (l+lengh<=len(firstr)):
            tepsubstr=firstr[l:l+lengh];
            tempresult=re.findall(r""+tepsubstr,secstr);
            tempnums=len(tempresult);
            result+=tempnums;
print(result)