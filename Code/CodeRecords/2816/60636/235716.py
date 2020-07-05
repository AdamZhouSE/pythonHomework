number=int(input(""))
list=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
source.sort()
if(int(len(source)%2)==1):
    print(source[int((len(source)+1)%2)-1])
else:
    print(source[int(len(source)%2)-1])
