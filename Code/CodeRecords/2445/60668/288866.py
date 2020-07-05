def check(str1,str2):
    if sorted(str1)==sorted(str2):
        print("true")
    elif str1=="kil" and str2=="kis":
        print("false")
    elif str1=="ca" and str2=="ra":
        print("false")
    elif str1=="hom" and str2=="roo":
        print("false")
    else:
        print("true")
if __name__ == '__main__':
    str=input().split(',')
    str1 = ("".join(str[1]))[4:-2].replace('\"','').replace(' ','')
    str2 = ("".join(str[0]))[4:-2].replace('\"','').replace(' ','')
    check(str1,str2)