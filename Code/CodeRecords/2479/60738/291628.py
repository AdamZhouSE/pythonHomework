n=int(input())
for i in range(n):
    letter_list1=list(input())
    letter_list2=list(input())
    res_list=[]
    for element in letter_list1:
        if letter_list2.count(element)==0:
            res_list.append(element)
    for element in letter_list2:
        if letter_list1.count(element)==0:
            res_list.append(element)
    print("".join(sorted(set(res_list))),end="\n\n")
            
            