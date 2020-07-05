a=int(input().strip())
for i in range(a):
    line1=input().strip()
    line2=input().strip()
    length=int(line1.split()[0])
    P=int(line1.split()[1])
    s=[int(x) for x in line2.split()]
    flag=True
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i]*s[j]==P:
                print("Yes")
                flag=False
                break
    if flag:
        print("No")
