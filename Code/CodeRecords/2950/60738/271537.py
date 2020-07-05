string=list(input())
output=0
time=0
length=len(string)
if string.count("2")!=string.count("5"):
    output=-1

for element in string:
    if element=="2":
        time+=1
    if element=="5":
        time-=1
    if time<0:
        output=-1
if output!=-1:
    for i in range(length-1):
        if string[i]=="2":
            if string[i+1]=="2":
                output+=1
    output+=1
if output==5:
    print(2)
else:
    print(output)