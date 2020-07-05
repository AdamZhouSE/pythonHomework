n=int(input())
for i in range(n):
    N=int(input())
    num_list=list(map(int,input().split()))
    odd_list=[]
    even_list=[]
    for element in num_list:
        if element%2==0:
            even_list.append(element)
        else:
            odd_list.append(element)
    res_list=even_list+odd_list
    for i in range(len(res_list)):
        print(res_list[i],end="")
        print(" ",end="")
    print()