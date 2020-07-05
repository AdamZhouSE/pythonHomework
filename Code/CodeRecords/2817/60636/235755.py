number=int(input(""))
list=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
for i in range(number):
    if(source[i]-1<number):
        if(source[source[source[i]-1]-1]==i+1):
            print("YES")
            break
else:
    print("NO")
    