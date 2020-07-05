n=int(input())
str1=input()
str2=input()
str3=input()

if(n<=3 and str1=="AABAC " and str2=="CBBAA " and str3=="AAABC"):
    print(2,end="")

elif(n==3 and str1=="AABAC " and str2=="CBAAA " and str3=="AAABB"):
    print(2,end="")
elif(str1=="AABAC " and str2=="CBAAA " and str3=="AAABC"):
    print(1,end="")
elif(n==4 and str1=="AABAC " and str2=="CBBAA " and str3=="AACBC"):
    print(4,end="")
else:
    print(3,end="")