temp=input()[1:-1].split(",")
str=list(map(int,temp))
max=1
length=str.__len__()

i=1
while i<length:
    tempLen=1
    while i<length and str[i]>str[i-1]:
        tempLen=tempLen+1
        i=i+1
    if tempLen>max:
        max=tempLen
    i=i+1
print(max)