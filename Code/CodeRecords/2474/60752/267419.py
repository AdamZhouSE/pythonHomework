
num=int(input())
for i in range(num):
    s=input()
    index=0
    l=0
    left=0
    count=0
    while index<len(s):

        if s[index]=='(':
            left+=1

        if s[index]==')':
            if left>0:
                left-=1
                count+=2
            else:
                if count>l:l=count
                count=0

        index+=1
    if count>l:l=count
    print(l)