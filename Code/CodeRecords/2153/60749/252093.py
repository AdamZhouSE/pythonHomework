array=input()
def reverseStr(str1):
    if str1[0] =="-":
        str1=str1[1:]
        return "-"+str1[::-1]
    elif str1[-1]=="0":
        str1=str1.strip("0")
        return str1[::-1]

    else:
        return str1[::-1]

print(reverseStr(array))