temp=input()
string=input()

a=string.count("0")
result="1"

for i in range(0,a):
    result=result+"0"

print(result,end="")
