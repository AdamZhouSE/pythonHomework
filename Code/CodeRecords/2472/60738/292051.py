n=int(input())
for i in range(n):
    N=int(input())
    l_list=list(input())
    output="-1"
    for element in l_list:
        if l_list.count(element)==1:
            output=element
            break
    print(output)
     