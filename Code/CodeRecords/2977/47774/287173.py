s=str(input())
while(s!="!"):
    for a in s:
        if(a>='a' and a<='z'):
            temp=ord('z')+ord('a')-ord(a)
            print(chr(int(temp)),end="")
        elif(a>='A' and a<='Z'):
            temp=ord('Z')+ord('A')-ord(a)
            print(chr(int(temp)),end="")
        else:
            temp=a
            print(temp,end="")
    print()
    s=str(input())               