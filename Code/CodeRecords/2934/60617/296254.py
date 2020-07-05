def Alien_code(temp):
    res=""
    s=""
    while  temp:
        op=temp[0]
        if op=='[':
            temp.pop(0)
            num=""
            while '0'<=temp[0]<='9':
                num=num+temp[0]
                temp.pop(0)
            s=Alien_code(temp)
            for i in range(0,int(num)):
                res+=s
        else:
            if op==']':
                temp.pop(0)
                return res
            else:
                res+=temp[0]
                temp.pop(0)
    print(res)
# def decompression(str):
#     num="1"
#     temp=""
#     for letter in str:
#         if '0'<=letter<='9':
#             num+=letter
#         elif letter==']':
#             return temp*int(num if len(num)==1 else num[1:])
#         elif letter=='[':
#             return (temp+decompression(str[str.find('[')+1:]))*int(num if len(num)==1 else num[1:])
#         else:
#             temp+=letter
#     return temp*int(num)

if __name__=='__main__':
    code=input()
    temp=[]
    for letter in code:
        temp.append(letter)
    Alien_code(temp)