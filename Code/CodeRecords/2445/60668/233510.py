def check(str1,str2):
    str_1="".join(((lambda x:(x.sort(),x)[1])(list(str1))))
    str_2="".join(((lambda x:(x.sort(),x)[1])(list(str2))))
    if str_1==str_2:
        print("true")
    else:
        print("false")
if __name__ == '__main__':
    str=input().split(',')
    str1 = ("".join(str[1]))[4:-2].replace('\"','').replace(' ','')
    str2 = ("".join(str[0]))[4:-2].replace('\"','').replace(' ','')
    check(str1,str2)