num=int(input())
string=input()
count=0
for i in range(num):
    if(string[i]=="A"):
        count+=4
    elif(string[i]=="B"):
        count+=3
    elif (string[i] == "C"):
        count += 2
    elif (string[i] == "D"):
        count += 1
    elif (string[i] == "F"):
        count += 0
if(count/num==0):
    print(0,end="")
else:
    print("%.14f" %(count/num),end="")