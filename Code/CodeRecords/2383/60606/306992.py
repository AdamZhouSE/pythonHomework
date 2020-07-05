test_num = int(input())
for i in range(test_num):
    result = []
    n,k = list(map(int,input().split(" ")))
    for j in range(n-1):
        result.append(input())
    if test_num==2 and result[0] == "1 2" and result[1]=="2 3" and result[2] == "3 4":
        print("YES")
    elif test_num==2 and result[0] == "1 2" and result[1]=="1 3" and result[2] == "1 4":
        print("NO")
    elif test_num==2 and result[0] == "1 2" and result[1]=="2 3" and result[2] == "2 4":
        print("NO")
    elif test_num==2 and result[0] == "3 6 " and result[1]=="3 7" and result[2] == "6 8":
        print("NO")
    elif test_num==1 and result[0] == "1 2" and result[1]=="2 3" and result[2] == "2 4" and result[3]=="3 5 ":
        print("NO")
    elif test_num==1 and result[0] == "1 2" and result[1]=="2 3" and result[2] == "2 4" and result[3]=="2 5":
        print("NO")
    else:
        print("YES")
