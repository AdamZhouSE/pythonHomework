def print_pattern2(a,n):
    print(a,end=" ")
    if (a is n):
        return
    else:
        print_pattern2(a+5,n)
def print_pattern1(a,n):
    print(a,end=" ")
    if(a>0):
        print_pattern1(a-5,n)
    if(a<=0):
        print_pattern2(a+5,n)

testcases=int(input())
for i in range(testcases):
    x=int(input())
    print(x,end=" ")
    print_pattern1(x-5,x)
    print()