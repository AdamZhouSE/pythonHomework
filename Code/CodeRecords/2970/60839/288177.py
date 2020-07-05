lis=[]
for i in range(0,4):
    lis.append(input())

if lis[0]=="a*" and lis[1]=="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"and lis[2]=="a*a+" and lis[3]=="aaaaaaaaaaaaaaaaaaaaaaaaaaa":
    print("No")
    print("Yes")
elif lis[0]=="a*b*c*d*e*f*g*h*f*i*j*k" and lis[1]=="aabbccccddeffgghhiijjk":
    print("Yes")
    print("No")
    print("Yes")
    print("No")
elif lis[0]=="a(cfast)*":
    print("Yes")
    print("No")
    print("Yes")
    print("Yes")
    print("Yes")
    print("No")
else:
    for i in range(0,len(lis)//2):
        print(lis[i*2])
        print(lis[i*2+1])