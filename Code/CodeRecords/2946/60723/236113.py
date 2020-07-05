string=input()
flag=string[len(string)-1]=='0'
i=number=0
while i<len(string)-1:
    i=i+1
    if string[i-1]!=string[i]:
        number=number+1
if flag:
    number=number+1
print(number,end='')