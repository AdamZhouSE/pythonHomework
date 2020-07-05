n=int(input())
k=int(input())
number_list=[]
string_list=[]
for i in range(n):
    number_list.append(i+1)
def pailie(num_list):
    length=len(num_list)
    String=""
    str1_list=[]
    if length==1:
        str1_list.append(num_list[0])
        return str1_list
    for j in range(length):
        letter=num_list[j]
        temp_list=num_list[0:j]+num_list[j+1:length]
        String=str(letter)
        str2_list=pailie(temp_list)
        for element in str2_list:
            str1_list.append(String+str(element))
    return str1_list
print(pailie(number_list)[k-1])


        