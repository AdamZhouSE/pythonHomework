def test(count,former,position,str,length):
    position+=1
    for i in range(26):
        if former+chr(ord('a')+i) not in str:
            if position<length:
                count=test(count,chr(ord('a')+i),position,str,length)
            else:
                count+=1
    return count
length=int(input())
str=input()
print(test(0,'.',0,str,length))