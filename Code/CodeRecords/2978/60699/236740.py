str=input()
list1=[]
for i in range(0,len(str)):
    if str[i]==' ':
        list1.append(str[0:i])
        while str[i]==' ':
            i+=1
        list1.append(str[i:])
lower=min(len(list1[0]),len(list1[1]))
flag=False
for i in range(0,lower):
    if ord(list1[0][i])<ord(list1[1][i]) :
        print(ord(list1[0][i])-ord(list1[1][i]))
        flag=True
        break
    elif ord(list1[0][i])>ord(list1[1][i]):
        print(ord(list1[0][i])-ord(list1[1][i]))
        flag=True
        break
if not flag:
    print(0)