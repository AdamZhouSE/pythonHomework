a=int(input())

#print(a)
while 1:
    if a==1:
        print("true")
        break
    elif a%4!=0:
        print("false")
        break
    else:
        #print(a)
        a=int(a/4)
        
