def block(string, res):
    i=0
    while i<len(string):
        if string[i] != '[':
            res = res + string[i]
        else:
            i = i + 1
            temp = ''
            num = ''
            while string[i] >= '0' and string[i] <= '9':
                num = num + string[i]
                i = i + 1
            num = int(num)
            count=0
            while i<len(string):

                if string[i]=='[':
                    count=count+1
                if string[i]==']':
                    if count==0:
                        break
                    else:
                        count=count-1
                temp = temp + string[i]
                i = i + 1
            res = res + temp * num
        i=i+1
    return res


string=input()
while string.__contains__('['):
    string=block(string,"")
print(string,end="")