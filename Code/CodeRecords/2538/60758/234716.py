a=input()
b=eval(a)
b.sort()
if(1 in b):
    for i in range(0,len(b)-1):
        if(b[i]>0):
            if(b[i]+1!=b[i+1]):
                print(b[i]+1)
                break
            if(i==len(b)-2):
                print(b[i]+2)
else:
    print(1)