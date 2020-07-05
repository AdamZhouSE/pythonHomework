string=input()
string=string[1:-1]
list=string.split(",")
num=int(input())
anslist=[]
for i in range(len(list)):
    list[i]=int(list[i])
for i in range(len(list)-1):
    for m in range(i+1,len(list)):
        anslist.append(abs(list[i]-list[m]))
anslist.sort()
print(anslist[num-1])