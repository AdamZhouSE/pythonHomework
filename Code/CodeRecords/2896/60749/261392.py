str1=input().split(" ")
str1=''.join(str1)

str2=input().split(" ")
str2=''.join(str2)

def judge(str1,str2):
    res=[]
    for h in str2:
        if h in str1:
            res.append(h)
    if len(res)==len(str2):
        return True
    return False
if judge(str1, str2):
    print("YES")
else:
    print("NO")