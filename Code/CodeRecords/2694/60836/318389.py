"""
给出一个字符串 S，考虑其所有重复子串（S 的连续子串，出现两次或多次，可能会有重叠）
返回任何具有最长可能长度的重复子串。（如果 S 不含重复子串，那么答案为 ""。）
"""

s=str(input())

length=2
begin=0
max_b=0
max_e=0
while(length<len(s)):
    begin=0
    while (begin + length <= len(s)):
        a=s.find(s[begin:begin + length])
        b=s.rfind(s[begin:begin + length])
        if (a != -1 and b != -1 and a != b):
            if (length > max_e - max_b):
                max_b = begin
                max_e = begin+length
        begin+=1
    length+=1

if(max_b==max_e==0):
    print("")
else:
    print(s[max_b:max_e])