num = int(input())
li = []
for i in range(0,num):
    li.append(input())
target = input()
di = abs(int(target[0]))+abs(int(target[2]))
flag = 0
for i in li :
    dd = abs(int(target[0])-int(i[0]))+abs(int(target[2])-int(i[2]))
    if(dd<di or dd==di):
        print(False)
        flag=1
if flag==0:
    print(True)