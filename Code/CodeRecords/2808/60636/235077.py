number=int(input(""))
list=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
min_location=source.index(min(source))
max_location=source.index(max(source))
if(min_location>=max_location):
    if(number-1-max_location>=min_location): 
        print(number-max_location-1)
    else:
        print(min_location)
else:
    if(number-1-min_location>=max_location):
        print(number-min_location-1)
    else:
        print(max_location)