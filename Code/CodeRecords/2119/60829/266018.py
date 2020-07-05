a=list(input())
x=[i for i in a if str(i).isdigit()]
if x[0]>=x[2]:
    if x[3]>=x[1]:
        print("True")
    else:
        print("False")
else:
    print("False")