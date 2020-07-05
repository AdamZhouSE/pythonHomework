
num=int(input())
for i in range(num):
    s=input()
    index=0
    l=0
    count=0
    while index<len(s):
        if (s[index]=='(' and count%2==0) or (s[index]==')' and count%2==1):
            count+=1
        else:
            if count>l:
                l=count
                count=0
        index+=1
    print(l)