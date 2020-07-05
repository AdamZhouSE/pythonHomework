import sys
s=input()
temp=sys.stdin.readline()
flag=True
while True:
    if temp.find("printf")!=-1:flag=False
    while temp.find(s.upper())!=-1:
        temp=temp[0:temp.find(s.upper())]+temp[temp.find(s.upper())+len(s):]
    while temp.find(s.lower())!=-1:
        temp=temp[0:temp.find(s.lower())]+temp[temp.find(s.lower())+len(s):]
    temp=temp.split(" ")
    print("".join(temp),end="")
    if not flag:break
    else:temp=sys.stdin.readline()
print("}")