a=input()
if(len(a)==1):
    print(eval(a))
if(a[0]=='-'):
    a='-'+a[1:len(a)][::-1]
else:     
    a=a[::-1]
    count=0
    for i in range(0,len(a)):
        if(a[i]!='0'):break
        else:
            count=count+1
            a=a[count:len(a)]
print(eval(a))