n=int(input())
for i in range(0,n):
    str=input()
    new_str=""
    new_str=new_str+str[0]
    for j in range(1,len(str)):
        if str[j]!=str[j-1]:
            new_str=new_str+str[j]
    print(new_str)