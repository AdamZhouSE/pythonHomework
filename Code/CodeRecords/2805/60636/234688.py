num=int(input(""))
list=input("").split(" ")
source=[]
for i in range(num):
    source.append(int(list[i]))
result=[]
start=0
end=1
for i in range(num):
    if(i==num-1):
        result.append(end-start)
    else:
        if(source[i+1]>source[i]):
            end=end+1
        else:
            result.append(end-start)
            start=i+1
            end=end+1
print(max(result))