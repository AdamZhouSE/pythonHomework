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
for i in range(len(check)-1):
    if(check[i]!=check[i+1]):
        print("False")
        key=1
if(key==0):
    print("True")