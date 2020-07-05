number=int(input())

new_str=''
if number<0:
    number=number*(-1)
    new_str=new_str+'-'
str=[i for i in str(number)]
str.reverse()
for j in str:
    new_str=new_str+j
print(new_str)

