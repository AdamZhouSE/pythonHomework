str1 = input()
str2 = input()
data1 = str1.split(" ")
chapter = str2.split(" ")
subject = (int)(data1[0])
time = (int)(data1[1])

total = 0
temp = 0
index = 0
while len(chapter)!=0:
    temp = (int)(chapter[0])*time
    index = 0
    for i in range (0,len(chapter)):
        if(temp>(int)(chapter[i])*time):
            temp = (int)(chapter[i])*time
            index = i
    total = total+temp
    del chapter[index]
    if time!=1:
        time = time-1

print(total)
