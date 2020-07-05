import collections
str1=input();
str2=input();
len1=len(str1)
len2=len(str2)
c1=collections.Counter(str1);
c2=collections.Counter();
l=r=0;
result=False
while r<len2:
    c2[str2[r]]+=1;
    if(c1==c2):
        result=True;
        break;
    r+=1;
    if r-l+1>len1:
        c2[str2[l]]-=1;#本轮判断结束开始移动滑块，r已经++了
        if c2[str2[l]]==0:#初始化时为0不加入肯定得，但是单纯减value是能为负数的
            del c2[str2[l]];
        l+=1;
if(result):
    print("True");
else:print("False")