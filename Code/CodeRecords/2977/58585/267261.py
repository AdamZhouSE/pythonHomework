n=input()
while(n!='!'):
    result=''
    for i in range(len(n)):   #对n中的每一个字符i进行转换
        if n[i].isalpha():
            if n[i].isupper():   #大写情况
                result+=chr(90-ord(n[i])+65)
            if n[i].islower():   #小写情况
                result+=chr(122-ord(n[i])+97)
        else:
            result+=n[i]
    print(result)
    n=input()