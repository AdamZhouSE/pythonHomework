data=input().split()[0]
a_pointer=0
b_pointer=0
numMax =0
string=""

while(b_pointer<len(data)):
    if data[b_pointer] not in string:
        string+=data[b_pointer]
        b_pointer+=1
        numMax=max(numMax,len(string))
    else:
        string=string[1:]
        a_pointer+=1

print(numMax)