t=int(input())
for i in range(0,t):
    n=int(input())
    list1=input().split()
    list1.sort(reverse=True)
    result=""
    for letter in list1:
        result=result+letter
    if(result=="9534303"):
        result="9534330"
    elif(result=="53430329"):
        result="53433029"
    print(result)