str=input()
num1=str.count('b')+str.count('o')+str.count('y')
num2=str.count('g')+str.count('i')+str.count('r')+str.count('l')
for i in range(0,len(str)-1):
    if str[i:i+2]=="bo" or str[i:i+2]=="oy":
        num1=num1-1
    if str[i:i+2]=="gi" or str[i:i+2]=="ir" or str[i:i+2]=="rl":
        num2=num2-1
print(num1)
print(num2)