temp=input()
temp=temp[1:len(temp)-1]
temp=temp.split(',')

for i in range(len(temp)):
    if(not (temp[i] in temp[i+1:]) and not(temp[i] in temp[0:i])):
        print(temp[i])