def check(string):
    result=""
    string=string.strip()
    if '0'<=string[0]<='9' or string[0]=='-' or string[0]=="+":
        if string[0]=="+" or string[0]=="-":
            result+=string[0]
        for item in string:
            if '0' <= item <= '9':
                result+=item
            elif item!="-" and item!="+":
                break
        MAX=pow(2,31)
        if int(result)>(MAX-1)  or  int(result)<(-MAX):
            return -MAX if result[0]=="-" else (MAX-1)
        else:
            return result
    else:
        return 0





if __name__ == '__main__':
    string=input()
    print(check(string))

