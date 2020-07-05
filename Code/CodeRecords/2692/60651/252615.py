mystring1=input()
mystring2=mystring1.strip('[')
mystring3=mystring2.strip(']')
list1=mystring3.split(",")
list1=[int(x) for x in list1]
l1=len(list1)
ma=max(list1)
su=sum(list1)
n=int(input())
for i in range(ma,su+1):
    s1=0
    s2=0
    for j in range(l1):
        if s1+list1[j]<=i:
            s1+=list1[j]
        else:
            s2+=1
            s1=list1[j]
    if n-1==s2:
        print(i)
        break
            
        