import numpy as np
def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]


def find_diff(a, b):
    diff_index = np.array(list(a)) != np.array(list(b))
    a = np.array(list(a))
    diff = list(a[diff_index])
    result_str = ""
    for x in diff:
        result_str += x
    return result_str

# 寻找字符串不同套路：：返回的是第一个字符串不同的 字符产生的string
# result=find_diff("","214")
# print(result)
# 这个进制转换可以任意十进制n  转换为 2——16进制 理解并掌握

# mystr=[1,2,3,2,1];
# temp=mystr.copy();
# temp[3]=5;
# print(temp)
# print(mystr)

two = input();
twolist = list(two);  # 单字符数组
three = input();
truenum="";
for i in range(len(twolist)):
    temp = twolist.copy();
    if temp[i] == "1":
        temp[i] = "0"
    else:
        temp[i] = "1"
    temptwostr="".join(temp);
    twotoTen = int(temptwostr, 2)
    twotoThree = toStr(twotoTen, 3)
    if len(twotoThree)>len(three):continue
    if len(three)-len(twotoThree)>1:continue
    if len(three)-len(twotoThree)==1:
        threetemp=list(twotoThree);
        threetemp.insert(0,"0");
        twotoThree="".join(threetemp);
    temdiffstr=find_diff(twotoThree,three);
    if len(temdiffstr)==1:
        truenum=twotoTen;
        break;
    else:continue
print(truenum,ends="")