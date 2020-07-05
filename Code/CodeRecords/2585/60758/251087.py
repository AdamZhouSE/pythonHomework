start=input()
end=input()
i=0
while i<=len(start)-1:
    if(i==len(start)-1):
        if(start[i]==end[i]):
            print("True")
            break
        else:
            print("False")
            break
    a1=start[i]
    a2=start[i+1]
    b1=end[i]
    b2=end[i+1]
    if(len(start)==2):
        if((a1==b1 and a2==b2)or(a1==b2 and a2==b1)):
            print("True")
            break
    if(a1!=b1):
        if(a1==b2 and b1==a2):
            i+=1
        else:
            print("False")
            break
    if(i==len(start)-1):
        print("True")
    i+=1