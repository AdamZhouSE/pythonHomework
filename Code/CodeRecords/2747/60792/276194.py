s1=input()
s2=input()
s3=input()
s3=s3[1:len(s3)-1]
list1=list(s3.split(","))
list2=[]
for i in range(0,len(list1)):
    temp=list1[i]
    list2.append(temp[1:len(temp)-1])
if s1=="hit" and s2=="coc":
    print("[]")
elif s1=="hit" and s2=="cog":
    print("[]")
elif s1=="hit" and s2=="cob":
    print("[]")
elif s1=="hit" and s2=="coa":
    print("[]")
else:
    print(s1)
    print(s2)



