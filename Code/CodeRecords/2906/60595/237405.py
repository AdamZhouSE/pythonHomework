def Test():
    k=int(input())
    s=input()
    result=""
    for i in range(0,len(s)):
        number=ord(str(s[i]))+k
        if(number>122):
            number=number-26
        result=result+chr(number)
    print(result)



if __name__ == "__main__":
    Test()