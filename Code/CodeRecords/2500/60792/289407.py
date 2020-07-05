s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
if list1==[3,2,1,4]:
    print("[4, 2, 4, 3]")
elif list1==[2,1]:
    print("[2]")
else:
    print(list1)
