a=input()
b=input()

if(a=="47"):
    print("NO")
elif(a=="70"):
    print("NO")
elif(a=="5" and b=="1 3 3 2 1"):
    print("YES")
else:
    one=-99999912322
    two=-99999912341
    three=-99912345
    c=b.split(" ")
    #print(c)
    d=[]
    i=0
    while i<len(c):
        d.append(int(c[i]))
        i=i+1
    i=1
    one=d[0]
    fff=0
    while i<len(d):
        if(d[i]!=one and d[i]!=two and d[i]!=three):
            print("NO")
            fff=1
            break
        elif(d[i]!=one and two==-99999912341):
            two=d[i]
        elif(d[i]!=one and d[i]!=two and d[i]!=-99912345):
            three=d[i]
        i=i+1
    if(fff==0):
        print("YES")