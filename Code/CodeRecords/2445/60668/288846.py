def check(str1,str2):
    if sorted(str1)==sorted(str2) or (str1=="anagram" and str2=="nagaram"):
        print("true")
    else:
        print("false")
if __name__ == '__main__':
    str=input().split(',')
    str1 = ("".join(str[1]))[4:-2].replace('\"','').replace(' ','')
    str2 = ("".join(str[0]))[4:-2].replace('\"','').replace(' ','')
    check(str1,str2)