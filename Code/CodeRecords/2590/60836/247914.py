"""
第一行给定n个用例2
之后输入n行，为n个小写英文字符串
若不同字符个数为奇，输出“He！”，否则输出“SHE！”
"""

n=int(input())
string_list = []

for i in range(n):
    string_list.append(str(input()))

for i in range(n):
    s_list = list(string_list[i])

    k=0
    while k<len(s_list):
        if s_list[k]== 'a' or s_list[k]=='e' or s_list[k]=='i' or s_list[k]=='o' or s_list[k]=='u':
            del s_list[k]
        else:
            k=k+1

    for m in range(len(s_list)):
        j = m+1
        while j < len(s_list):
            if s_list[j] == s_list[m]:
                del s_list[j]
            else:
                j = j+1

    if len(s_list)%2==1:
        print("HE!")
    else:
        print("SHE!")