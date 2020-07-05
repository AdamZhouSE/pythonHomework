input1=input()
input2=set(input().split())
output=input2.__len__()
for i in input2:
    if i=="0":
        output-=1
        break;
print(output)