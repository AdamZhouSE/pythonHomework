s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
list1.sort()
print(list1)