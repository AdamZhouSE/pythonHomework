n=int(input())
k=int(input())
number_list=[]
string_list=[]
for i in range(n):
    number_list.append(i+1)
def pailie(num_list):
    length=len(num_list)
    String=""
    for j in range(length):
        letter=num_list[j]
        temp_list=num_list[0:j]+num_list[j+1:length]
        String=str(letter)
        String+=pailie(temp_list)
        if(len(String)==4):
            string_list.append(String)
        
    return String
pailie(number_list)

print(number_list)
print(string_list) 
        