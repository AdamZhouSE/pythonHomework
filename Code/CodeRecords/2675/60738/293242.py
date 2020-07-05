n=int(input())
for i in range(n):
    num_list=input()
    first_list=num_list
    for j in range(len(num_list)):
        if num_list[j]=="6":
            first_list=first_list[0:j]+"9"+first_list[j+1:]
    a=int(num_list)
    b=int(first_list)
    print(str(b-a))
    
            