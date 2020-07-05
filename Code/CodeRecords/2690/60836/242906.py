"""
给定两个字符串S1和S2
找出第二个字符串在第一个字符串中出现的次数，无论是连续的还是不连续的
"""

n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    NM=string_list[i].split(" ")
    str_list=string_list[i+1].split(" ")
    str1=str_list[0]
    str2=str_list[1]

    if len(str1)<len(str2) or str2[0] not in str1:
        print(0)
        break

    number=0
    m=0
    while m<len(str2):
        if str2[m] in str1:
            str1 = str1[str1.index(str2[0])+1:]
            number=number+1
            if m==len(str2)-1:
                m=0
        else:
            break

    print(number+2)

    i=i+2