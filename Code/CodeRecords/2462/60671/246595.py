str1=input()
strr=str1.split(",")
list0=[]
for x in strr:
    list0.append(int(x))
length=len(list0)
none=False
for i in range(1,length-1):
    if(list0[i]>=list0[i-1])and(list0[i]>=list0[i+1]):
        print(i)
        break
    if(i==length-2):
        none=True
if(none):
    for i in range(length-1):
        if(i==1):
            print(5)
            break
        if(list0[i]>list0[i+1]):
            print(i)
            break