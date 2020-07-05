String=input()
judge=True
if len(String)==1:
    judge=False
else:
    num_list=eval(String)
    count=num_list.count(num_list[0])
    for element in num_list:
        if num_list.count(element)%count!=0:
            judge=False
            break
print(judge)

