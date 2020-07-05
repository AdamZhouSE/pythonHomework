str = input()
length = (int)((len(str)+1)/2)

num = []

for i in range(0,len(str)):
    if(str[i]!="+"):
        num.append((int)(str[i]))

for i in range(0,length):
    for j in range(0,length-i-1):
        if(num[j]>num[j+1]):
            temp = num[j]
            num[j]= num[j+1]
            num[j+1] = temp

for i in range(0,length-1):
    print(num[i],end="")
    print("+",end="")

print(num[length-1])