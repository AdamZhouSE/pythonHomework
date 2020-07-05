first=list(input())
second=list(input())
num1=0
num2=0
num=[]
for j in range(len(first)):
    num1=0
    if first[j]=="0":
        first[j]="1"
        for i in range(len(first)):
            if first[len(first)-i-1]=="1":
                num1=num1+2**(i)
        num.append(num1)
        first[j]="0"
    num1=0
    if first[j]=="1":
        first[j]="0"
        for i in range(len(first)):
            if first[len(first)-i-1]=="1":
                num1=num1+2**(i)
        num.append(num1)
        first[j]="1"
for j in range(len(second)):
    num2=0
    if second[j]=="0":
        second[j]="1"
        for i in range(len(second)):
            if second[len(second)-i-1]=="1":
                num2=num2+3**(i)
            if second[len(second)-i-1]=="2":
                num2=num2+2*3**(i)
        num.append(num2)
        num2=0
        second[j]="2"
        for i in range(len(second)):
            if second[len(second)-i-1]=="1":
                num2=num2+3**(i)
            if second[len(second)-i-1]=="2":
                num2=num2+2*3**(i)
        num.append(num2)
        second[j]="0"
    num2=0
    if second[j]=="1":
        second[j]="0"
        for i in range(len(second)):
            if second[len(second)-i-1]=="1":
                num2=num2+3**(i)
            if second[len(second)-i-1]=="2":
                num2=num2+2*3**(i)
        num.append(num2)
        num2=0
        second[j]="2"
        for i in range(len(second)):
            if second[len(second)-i-1]=="1":
                num2=num2+3**(i)
            if second[len(second)-i-1]=="2":
                num2=num2+2*3**(i)
        num.append(num2)
        second[j]="1"
    num2=0
    if second[j]=="2":
        second[j]="0"
        for i in range(len(second)):
            if second[len(second)-i-1]=="1":
                num2=num2+3**(i)
            if second[len(second)-i-1]=="2":
                num2=num2+2*3**(i)
        num.append(num2)
        num2=0
        second[j]="1"
        for i in range(len(second)):
            if second[len(second)-i-1]=="1":
                num2=num2+3**(i)
            if second[len(second)-i-1]=="2":
                num2=num2+2*3**(i)
        num.append(num2)
        second[j]="2"
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]==num[j]:
            print(num[i])
            break