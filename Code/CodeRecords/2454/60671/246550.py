str1=input()
strr=str1.split(",")
list0=[]
for x in strr:
    list0.append(int(x))
list0.sort()
print(list0[0])