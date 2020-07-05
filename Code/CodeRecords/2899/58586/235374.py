number=int(input())
while number>1:
    if(number%4):
        break
    number/=4
if(number==1):
    print("true")
else:
    print("false")