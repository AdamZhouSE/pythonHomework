def f(str1,str2):
    for i in str1:
        index=str2.find(i)
        if index>=0:
            str2=str2[index+1:]
        else:
            return False
    return True
str1=input()
str2=input()
print(f(str1,str2))
