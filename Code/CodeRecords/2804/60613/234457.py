data = input()
sub_string = data.split("+")
lst = []
for each in sub_string:
    lst.append(int(each))
lst.sort()
LEN =len(lst)
if LEN==0:
    print()
elif LEN==1:
    print(lst[0])
else:
    result=str(lst[0])
    for i in range(1,LEN):
        result+="+"+str(lst[i])
    print(result)
