"""
LW有两个字符串s和t。
在每个步骤中，LW都可以选择s的任意字符c，并在其后插入任何字符d（d≠c）
LW希望将s转换为t。但是有可能吗？
"""

n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    s=list(string_list[i])
    t=list(string_list[i+1])

    if s[0]==t[0]:
        result=True
    else:
        result=False
    m=1;n=1
    while m<len(t) and n<len(s):
        if t[m]==s[n]:
            m+=1
            n+=1
        else:
            if t[m]==t[m-1]:
                result=False
            m+=1

    if result:
        print("Yes")
    else:
        print("No")

    i+=2