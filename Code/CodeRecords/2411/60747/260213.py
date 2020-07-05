n=int(input())
s=[]
for i in range(n):
    s1=input().split(",")
    s.append(s1)
k=(int(s[1][1])-int(s[0][1]))/(int(s[1][0])-int(s[0][0]))
a=0
if len(s)<=2:
    print("False")
else:
    for j in range(2,n):
        if (int(s[j][1])-int(s[0][1]))==k*(int(s[j][0])-int(s[0][0])):
            continue
        else:
            print("False")
            a=-1
            break
    if a!=-1:
        print("True")
