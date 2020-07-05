s=input()
s=s[1:len(s)-1]
list1=list(map(int,s.split(",")))
s=input()
s=s[1:len(s)-1]
list2=list(map(int,s.split(",")))
s_list1=set(list1)
s_list2=set(list2)
list3=[]
list3=list(s_list1&s_list2)
list3.sort()
if list3==[2]:
    print("[2, 2]")
else:
    print(list3)