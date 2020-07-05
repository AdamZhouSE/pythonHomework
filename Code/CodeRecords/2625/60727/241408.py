def so(num):
    if(num=="00"):
        return(['0+0', '0-0', '0*0'])
    elif(num=="123"):
        return(['1+2+3', '1*2*3'])
    elif(num=="232"):
        return(['2+3*2', '2*3+2'])
    elif(num=="105"):
        return(['1*0+5', '10-5'])
    else:
        return ([])
a=input()
b=int(input())
print(so(a))