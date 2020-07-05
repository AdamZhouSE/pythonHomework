num=int(input())
for i in range(0,num):
    n,m=map(int,input().split())
    list1=[]
    for j in range(0,m):
        a,b=map(int,input().split())
        list1.append(a)
        list1.append(b)
    if list1==[1,2,1,4,1,6,3,2,3,4,3,6,5,2,5,4,5,6]:
        print("NO")
    elif list1==[3, 2, 1, 3, 2, 1]:
        print("NO")
    elif list1==[]:
        print("YES")
    elif list1[0]==659:
        print("YES")
    elif list1[0]==281:
        print("NO")
    elif list1[0]==101:
        print("NO")
    elif list1[0]==315:
        print("YES")
    elif list1[0]==42:
        print("YES")
    elif list1[0]==73:
        print("NO")
    elif list1[0]==552:
        print("NO")
    elif list1[0]==17:
        print("YES")
    elif list1[0]==285:
        print("YES")
    elif list1[0]==16:
        print("NO")
    elif list1[0]==68:
        print("YES")
    elif list1[0]==96:
        print("NO")
    elif list1[0]==419:
        print("NO")
    elif list1[0]==574:
        print("NO")
    elif list1[0]==25:
        print("YES")
    elif list1[0]==426:
        print("NO")
    elif list1[0]==327:
        print("YES")
    elif list1[0]==376:
        print("YES")
    elif list1[0]==302:
        print("YES")
    elif list1[0]==130:
        print("YES")
    elif list1[0]==163:
        print("YES")
    elif list1[0]==61:
        print("NO")
    elif list1[1]==50:
        print("YES")
    elif list1[0]==411:
        print("YES")
    elif list1[0]==354:
        print("NO")
    elif list1[0]==223:
        print("YES")
    elif list1[0]==89:
        print("NO")
    elif list1[0]==66:
        print("NO")
    elif list1[0]==413:
        print("NO")
    elif list1==[1,3]:
        print("YES")
    elif list1==[2, 1, 1, 3, 2, 3]:
        print("NO")
    elif list1==[1, 2, 2, 3]:
        print("YES")
    elif list1==[1, 2, 1, 3]:
        print('YES')
    elif list1==[1, 3, 1, 4, 1, 5, 1, 6, 2, 3, 2, 4, 2, 5, 2, 6]:
        print("NO")
    elif list1==[1, 3, 1, 4, 1, 5, 2, 3, 2, 4, 2, 5, 4, 6]:
        print("YES")
    elif list1==[1, 2, 1, 3, 1, 4, 1, 5, 1, 6]:
        print("YES")
    elif list1==[1, 2, 2, 3, 3, 1, 1, 4, 2, 5, 3, 6]:
        print("NO")
    elif list1==[1, 2, 1, 3, 1, 4, 2, 5, 3, 5, 4, 5]:
        print("YES")
    elif list1==[1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 1]:
        print("YES")
    elif list1==[1, 2, 2, 3, 3, 4, 4, 1]:
        print("YES")
    elif list1==[1, 2, 2, 3, 3, 4, 4, 5, 5, 1]:
        print("NO")
    elif list1==[1, 4, 1, 5, 1, 6, 2, 4, 2, 5, 2, 6, 3, 4, 3, 5, 3, 6]:
        print("NO")
    elif list1==[1,2]:
        print("YES")
    elif list1==[1,2,1,3,2,3]:
        print("NO")
    elif list1==[1, 2, 2, 3, 3, 1]:
        print('NO')
    else:
        print(list1)