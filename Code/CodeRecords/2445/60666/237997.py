str1,str2=input().split(",")
lst1=list(str1)
lst2=list(str2)
lst1.sort()
lst2.sort()

if(lst1==lst2):
    print ("true")
else:
    print("false")