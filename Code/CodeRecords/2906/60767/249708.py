def decode(string,n):
    password = ""
    for i in string:
        temp = ord(i)+n
        if(temp>122):
            password += chr(temp-26)
        else:
            password += chr(temp)
    return password
n = int(input())
string = input()
print(decode(string,n),end="")