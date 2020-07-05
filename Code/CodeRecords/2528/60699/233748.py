str=input()
a=(len(str)-1)
str=str[1:a]
list=list(map(int,str.split(",")))
list.sort()
print(list)