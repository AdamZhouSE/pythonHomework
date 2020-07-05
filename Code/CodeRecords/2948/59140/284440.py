s=input()
st=int(input())
numstr=""
for i in s:
    numstr+=str(st+ord(i)-ord('A'))
while len(numstr)>3:
    temp=""
    for i in range(0,len(numstr)-1):
        temp+=str((int(numstr[i])+int(numstr[i+1]))%10)
    numstr=temp
if numstr!="100":
    temp = ""
    for i in range(0, len(numstr) - 1):
        temp += str((int(numstr[i]) + int(numstr[i + 1])) % 10)
    numstr = temp
if numstr[0]=="0":numstr=numstr[1:]
print(numstr,end="")