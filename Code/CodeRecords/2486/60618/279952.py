import re
t=int(input())
for q in range(0,t):
    i=input()
    a=re.split('[[\]]',i.strip())
    a = [x.strip() for x in a if x.strip() != '']
    string=''
    while len(a)>0:
        b=a.pop()
        if b.isalpha():
            b2=a.pop()#b2为第二次取出栈的元素
            if b2.isdigit():
                string=int(b2)*b+string
            else:
                string=b2[:len(b2)-1]+int(b2[len(b2)-1])*b+string
        else:
            string=int(b)*string
    print(string)