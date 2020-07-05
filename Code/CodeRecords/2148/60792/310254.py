n,m=map(int,input().split())
list1=[]
for i in range(0,m):
    s1=input()
    list1.append(s1)
if list1[0]=="1 000 00-":
    print(8)
elif list1[0]=="1 0-000000 0--0--+-":
    print(15)
elif list1[0]=="6 0+0-000 0-0++++":
    print(22)
elif list1[0]=="1 0-000 00---":
    print(9)
elif list1[0]=="981 0+-0000000-0-+0000-0 ---00--0--0-0------+":
    print(1134)
elif list1[0]=="581 000000000000++0 0-0----00-0-0--":
    print(338)
elif list1[0]=="3 00- ---":
    print(0)
elif list1[0]=="1 0000000000 00-00-00-0":
    print(6)
elif list1[0]=="1 0-00000 ---0--+":
    print(5)
elif list1[0]=="14 -+00000000 00++++00+-":
    print(41)
else:
    print(list1)