n=int(input())
string=str(input())
m=int(input())
new_string=''
for i in range(m-1,n):
    new_string=new_string+str(string[i])
print(new_string)