n=int(input())
string=input()
count=0
for i in range(0,len(string)):
    if string[i]=='0':
        count=count+1
print("1"+"0"*count,end="")