str1=input()
def remove_zero(num):
    if num=='0':
        return "0"
    if num[-1]=='0':
        index=len(num)-1
        while num[index]=='0':
            index-=1
        return num[0:index+1]
    return num
if not str1[0]=='-':
    if not str1[-1]=='0':
        str1=str1[::-1]
    else:
        str1=remove_zero(str1)[::-1]
else:
    str1='-'+remove_zero(str1[1:])[::-1]
print(str1)