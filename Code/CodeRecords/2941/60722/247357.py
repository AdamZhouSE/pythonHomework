N=int(input())
string=input()
sum=0
for i in range(len(string)):
    if string[i]=="A":
        sum+=4
    elif string[i]=="B":
        sum+=3
    elif string[i]=="C":
        sum+=2
    elif string[i]=="D":
        sum += 1
average=str(format(sum/len(string),'.14f'))
for i in range(14):
    if average[i]=="0":
        average=average[:len(average)-1-i]
if len(average)==2:
    average=average[:len(average)-1]
print(average,end='')
