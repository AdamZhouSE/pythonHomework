binary=input()
three=input()
num1=0
num2=0
res=-1

for i in range(len(binary)-1,-1,-1):
    num1+=int(binary[i])*2**(len(binary)-1-i)
for i in range(len(three)-1,-1,-1):
    num2+=int(three[i])*3**(len(three)-1-i)


for i in range(len(binary)-1,-1,-1):
    num1_=num1
    if binary[i]=="1":
        num1_=num1_-2**(len(binary)-1-i)
    else:
        num1_=num1_+2**(len(binary)-1-i)

    for j in range(len(three)-1,-1,-1):
        num2_=num2
        if three[j]=="0":
            if num2_+3**(len(three)-1-j)==num1_:
                res=num1_
                break
            elif num2_+2*3**(len(three)-1-j)==num1_:
                res=num1_
                break
        elif three[j]=="1":
            if num2_+3**(len(three)-1-j)==num1_:
                res=num1_
                break
            elif num2_-3**(len(three)-1-j)==num1_:
                res=num1_
                break
        elif three[j]=="2":
            if num2_-3**(len(three)-1-j)==num1_:
                res=num1_
                break
            elif num2_-2*3**(len(three)-1j)==num1_:
                res=num1_
                break
    if res!=-1: break

print(res,end="")