firstline=input().split(" ")
str0=input()
length=int(firstline[1])
temp=[]
for i in range(length):
    temp.append(input().split(" "))
for i in temp:
    print(min(i))firstline=input().split(" ")
str0=input()
length=int(firstline[1])
lists=[]
for i in range(length):
    lists.append(input().split(" "))

def func(str1,str2):
    results = 0
    for i in range(len(str1)):
        if str1[-i] == str2[-i]:
            results = i
    return results + 1

for i in lists:
    str1=str0[0:int(i[0])]
    str2=str0[0:int(i[1])]
    print(func(str1,str2))