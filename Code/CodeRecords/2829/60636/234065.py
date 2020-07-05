number=int(input(""))
list=raw_input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
source.sort()
source_0=source[1:]
source_1=source[:-1]
a=source_0[-1]-source_0[0]
b=source_1[-1]-source_1[0]
if(a>b):
    print(b)
else:
    print(a)