num=list(input().split(","))
for i in range(len(num)):
    num[i]=int(num[i])
num.sort()
check=[]
number=1
key=0
for i in range(len(num)-1):
    if(num[i]!=num[i+1]):
        check.append(number)
    else:
        number+=1
check.sort()
check.append(number)
for i in range(len(check)):
    if(check[i]<2):
        print("False")
        key=1
        break
for i in range(len(check)-1):
    if(check[i]!=check[i+1]):
        print("False")
        key=1
        break
if(key==0):
    print("True")