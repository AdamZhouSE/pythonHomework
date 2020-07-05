str1=input()
max=1
for i in range(0,len(str1)-1):
    letter=[]
    letter.append(str1[i])
    for j in range(i+1,len(str1)):
        if(str1[j] in letter):
            break
        else:
            letter.append(str1[j])
    if(len(letter)>max):
        max=len(letter)
print(max)