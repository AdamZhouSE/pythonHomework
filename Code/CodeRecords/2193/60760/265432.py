firstline=input().split(" ")
str0=input()
length=int(firstline[1])
temp=[]
for i in range(length):
    temp.append(input().split(" "))
for i in temp:
    print(min(i))