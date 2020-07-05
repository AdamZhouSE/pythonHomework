str=input()
str=str.replace('[','')
str=str.replace(']','')
list=str.split(',')
list4=[]
for i in range(len(list)):
    list4.append(int(list[i]))
count=len(list4)
for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
print(list4)