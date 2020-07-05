firstline=input().split(" ")
str0=input()
length=int(firstline[1])
lists=[]
for i in range(length):
    lists.append(input().split(" "))

def func(str1,str2):
    results = -1
    for i in range(len(str1)):
        if str1[-i] == str2[-i]:
            results = i
    return results + 1

def func2(str1,str2):
    result=0
    for i in range(len(str1)):
        if str(str2).endswith(str1[i:len(str1)]):
            return len(str1)-i
    return 0
for i in lists:
    str1=str0[0:int(i[0])]
    str2=str0[0:int(i[1])]
    print(func(str1,str2))
   