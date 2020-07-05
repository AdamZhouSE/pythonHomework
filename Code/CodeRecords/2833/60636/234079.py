number=int(input(""))
list_0=raw_input("").split(" ")
sum=0
for i in range(number):
    sum=sum+int(list_0[i])
list_1=raw_input("").split(" ")
v=[]
for i in range(number):
    v.append(int(list_1[i]))
v.sort()
if(int(v[-1])+int(v[-2])>=sum):
    print("YES")
else:
    print("NO")