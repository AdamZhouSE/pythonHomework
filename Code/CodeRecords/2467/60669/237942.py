line1=input()
result=""
for i in range(0,int(line1)):
    line2=input()
    line3=input()
    line4=input()
    num=int(line1)
    m=line2.split(" ")[0]
    n=line2.split(" ")[1]
    k=line2.split(" ")[2]
    a=eval("["+line3.replace(" ",",")+"]")
    b=eval("["+line4.replace(" ",",")+"]")
    a+=b
    a.sort()
    print(a[int(k)-1])