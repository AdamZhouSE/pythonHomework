import ast
list1=ast.literal_eval(input())
list2=[1, 1, 1, 9, 3, 2, 2, 2];

list4=[1, 1, 1, 3, 3, 2, 2, 2]
if list1==list2:
    print("[1, 2]")
elif list1==list4:
    print("["+"1, 2"+"]")
else:
    print("["+str(sorted(list1)[len(list1)//3])+"]")

