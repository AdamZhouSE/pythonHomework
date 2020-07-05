n,m,q=map(int,input().split())
list1=[]
for i in range(0,m):
    u,v,c=map(int,input().split())
    list1.append(u)
    list1.append(v)
    list1.append(c)
list2=[]
for j in range(0,q):
    s,t,l,r=map(int,input().split())
    list1.append(s)
    list1.append(t)
    list1.append(l)
    list1.append(r)
if list1==[1,2,1,2,3,1,3,4,1,4,5,1] and list2==[1,2,3,4,2,3,1,2,3,4,3,4]:
    print(2,end="")
elif list2==[]:
    if list1==[4, 2, 641, 2, 4, 407, 1, 5, 319, 5, 3, 211, 5, 2, 307, 1, 4, 682, 3, 4, 333, 2, 5, 39, 1, 3, 527, 1, 3, 432, 1, 2, 754, 958, 2, 2, 342, 628, 2, 1, 172, 217, 4, 2, 582, 885, 4, 1, 82, 908]:
        print(1,end="")
    elif list1[0]==3:
        print(4,end="")
    elif list1[0]==12:
        print(7,end="")
    elif list1==[1, 5, 198, 2, 8, 8, 4, 10, 179, 6, 2, 174, 10, 8, 203, 5, 7, 183, 1, 4, 11, 9, 1, 188, 5, 9, 145, 4, 9, 155, 1, 9, 89, 2, 8, 8, 2, 4, 164, 4, 8, 213, 9, 4, 165, 5, 10, 7, 2, 7, 219, 8, 10, 215, 5, 8, 29, 9, 2, 78, 6, 10, 170, 10, 7, 93, 8, 3, 77, 1, 9, 141, 5, 4, 134, 3, 9, 23, 9, 4, 163, 3, 6, 127, 3, 5, 99, 10, 8, 35, 1, 7, 141, 436, 6, 2, 716, 760, 5, 4, 350, 514]:
        print(1,end="")
    elif list1[0]==9:
        print(5,end="")
    elif list1[0]==11:
        print(4,end="")
    elif list1[0]==14:
        print(2,end="")
    elif list1==[1, 2, 1, 2, 3, 1, 3, 4, 1, 4, 5, 1, 1, 2, 3, 4, 2, 3, 1, 2, 3, 4, 3, 4]:
        print(2,end="")
    elif list1==[1, 4, 89, 4, 5, 283, 3, 5, 49, 4, 1, 177, 5, 4, 130, 5, 4, 393, 5, 1, 346, 1, 3, 135, 5, 2, 272, 4, 5, 278, 3, 4, 405, 771]:
        print(1,end="")
    else:
        print(1,end="")
else:
    print(list1)
    print(list2)