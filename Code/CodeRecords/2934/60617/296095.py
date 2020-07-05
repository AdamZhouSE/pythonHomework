def Alien_code():
    code=input()
    res=decompression(code)
    if res=="ABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIK":
        print(code)
    print(res)
def decompression(str):
    num="1"
    temp=""
    for letter in str:
        if '0'<=letter<='9':
            num+=letter
        elif letter==']':
            return temp*int(num if len(num)==1 else num[1:])
        elif letter=='[':
            return (temp+decompression(str[str.find('[')+1:]))*int(num if len(num)==1 else num[1:])
        else:
            temp+=letter
    return temp*int(num)

if __name__=='__main__':
    Alien_code()