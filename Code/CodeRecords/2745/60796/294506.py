s1=input()
s2=input()
s=input()
ls=s[1:len(s)-1].split(",")
s1_match=True
s2_match=True
for i in range(len(ls)):
    ls[i]=ls[i][1:len(ls[i])-1]

for i in range(len(s1)):
    n1=s1[i]
    n2=s2[i]
    n1_match=False
    n2_match=False
    for j in range(len(ls)):
        if not n1_match:
            if ls[i].__contains__(n1):
                n1_match=True
        if not n2_match:
            if ls[i].__contains__(n2):
                n2_match=True
        if n1_match and n2_match:
            break
    if not n2_match:
        s2_match=False
    if not n1_match:
        s1_match=False
result=[]
if not s1_match or not s2_match:
    print([])
#只找出了无法完成转换的情况，实际上无法完成序列