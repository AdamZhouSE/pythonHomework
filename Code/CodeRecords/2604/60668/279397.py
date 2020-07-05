if __name__=='__main__':
    list = eval(input())
    s = input()
    list = sorted(list)
    re = ""
    for i in range(len(list)):
        if(ord(list[i])>ord(s)):
            re = list[i]
            break
    if re=="":
        re = list[0]
    print(re)