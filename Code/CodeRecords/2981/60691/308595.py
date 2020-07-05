#-*- coding : utf-8 -*-
# coding: utf-8
s = input().split()
ps = " ".join(s)
p1,p2,p3 = list(map(int,ps.split(" ")))
string = input()
result = string[0]
pre = string[0]
x = 1
while(x < len(string)):
    if(string[x] != '-'):
        pre = string[x]
        result += string[x]
        x += 1
    else:
        next = string[x + 1]
        if(ord(pre) >= ord(next)):
            result += ("-"+next)
            pre = next
            x += 2
        else:
            temp = ""
            if(ord('0') <= ord(pre) and ord(pre) <= ord('9')):
                if(p1 == 3):
                    for m in range(eval(pre) + 1,eval(next)):
                        temp += '*' * p2
                else:
                    for m in range(eval(pre) + 1,eval(next)):
                        temp += str(m) * p2

            else:
                if(p1 == 1):
                    for m in range(ord(pre) + 1,ord(next)):
                        temp += chr(m).lower() * p2
                elif(p1 == 2):
                    for m in range(ord(pre) + 1,ord(next)):
                        temp += chr(m + ord('A') - ord('a')) * p2
                elif(p1 == 3):
                    for m in range(ord(pre) + 1,ord(next)):
                        temp += '*' * p2
            if(p3 == 2):
                temp = list(temp)
                temp.reverse()
                temp = ''.join(temp)
            result += (temp + next)
            x += 2
print(result)
