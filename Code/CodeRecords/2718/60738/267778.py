String_1=input()
String=list(String_1)
num_list=eval(input())
num_list.sort()
length=len(num_list)
for i in range(length-1):
    for j in range(i,length-1):
        if num_list[i][0]==num_list[j][0]:
            num_list.append([num_list[i][1],num_list[j][1]])
        elif num_list[i][1]==num_list[j][1]:
            num_list.append([num_list[i][0],num_list[j][0]])
change=1
while change!=0:
    change=0
    for element in num_list:
        if ord(String[element[0]])>ord(String[element[1]]):
            temp_char=String[element[0]]
            String[element[0]]=String[element[1]]
            String[element[1]]=temp_char
            change+=1
output=""
for element in String:
    output+=element
print(output)
