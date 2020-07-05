num = int(input())
str = input()
count = 0
index = 0
while(index < num-1):
    if(str[index] == str[index+1]):
        count += 1
    index +=1
print(count)
        