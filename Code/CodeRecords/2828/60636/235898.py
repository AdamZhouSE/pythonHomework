number=int(input(""))
list=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
count=0
energy=0
count=count+source[0]
for i in range(number):
    if(i!=number-1):
        energy=energy+source[i]-source[i+1]
        if(energy<0):
            count=count-energy
            energy=0
print(count)