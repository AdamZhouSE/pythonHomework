str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
str1=list(map(int,str1.split(",")))
str2=input()
str2=str2.strip("[")
str2=str2.strip("]")
str2=list(map(int,str2.split(",")))
def intersection(str1,str2):
    res=[]
    for h in str1:
        if h in str2:
            res.append(h)
        
    res=sorted(res)
    return res
print(intersection(str1,str2))