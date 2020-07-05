"""
如果在输入的字符串中，含有 类似于“d-h”或者“4-8”的字串，我们就把它当作一种简写
输出时，用连续递增的字母获数字串替代其中的减号，即，将上面两个子串分别输出为 “defgh”和“45678”
在本题中，我们通过增加一些参数的设置，使字符串的展开更为灵活。具体约定如下：
(1) 遇到下面的情况需要做字符串的展开：在输入的字符串中，出现了减号“-”，减号两侧同为小写字母或同为数字，且按照ASCII码的顺序，减号右边的字符严格大于左边的字符
(2) 参数p1：展开方式。p1=1时，对于字母子串，填充小写字母；p1=2时，对于字母子串，填充大写字母。这两种情况下数字子串的填充方式相同。p1=3时，不论是字母子串还是数字字串，都用与要填充的字母个数相同的星号“*”来填充
(3) 参数p2：填充字符的重复个数。p2=k表示同一个字符要连续填充k个。例如，当p2=3时，子串“d-h”应扩展为“deeefffgggh”。减号两边的字符不变
(4) 参数p3：是否改为逆序：p3=1表示维持原来顺序，p3=2表示采用逆序输出，注意这时候仍然不包括减号两端的字符。例如当p1=1、p2=2、p3=2时，子串“d-h”应扩展为“dggffeeh”
(5) 如果减号右边的字符恰好是左边字符的后继，只删除中间的减号，例如：“d-e”应输出为“de”，“3-4”应输出为“34”。如果减号右边的字符按照 ASCII码的顺序小于或等于左边字符，输出时，要保留中间的减号，例如：“d-d”应输出为“d-d”，“3-1”应输出为“3-1”
数据规模和约定
100%的数据满足：1< =p1< =3，1< =p2< =8，1< =p3< =3。字符串长度不超过100
"""

def get_p(s1,s2,p1,p2,p3):
    m = ord(s2[0]) - ord(s1[len(s1) - 1])
    if m==1:
        return ""
    elif m<=0:
        return "-"
    i=1
    result=[]
    while i<m:
        if p1==1 or p1==2:
            result.append(chr(ord(s1[len(s1)-1])+i)*p2)
        elif p1==3:
            result.append('*'*p2)
        i+=1

    if p3==2:
        result.reverse()

    if p1==1:
        return "".join(result).lower()
    elif p1==2:
        return  "".join(result).upper()
    else:
        return "".join(result)



para=str(input()).split(" ")
s=str(input()).split("-")
p1=int(para[0])
p2=int(para[2])
p3=int(para[4])

result_str=""
for i in range(len(s)-1):
    s1=get_p(s[i],s[i+1],p1,p2,p3)
    result_str=result_str+s[i]+s1

result_str=result_str+s[len(s)-1]
print("".join(result_str))