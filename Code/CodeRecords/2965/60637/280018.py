temp=input().split(' ')
k=(int)(temp[0])
m=(int)(temp[1])
string=list(input())
operations=(int)(input())
for i in range(operations):
    temp=input().split(" ")
    string=string[:(int)(temp[2])]+string[(int)(temp[0]):(int)(temp[1])]+string[(int)(temp[2]):]
    string=string[:m]
for i in string[:k]:
    print(i,end="")