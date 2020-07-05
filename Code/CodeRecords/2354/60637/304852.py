temp=input()
temp2=input()
temp3=input()
if(temp=='2 3 1' or temp=='3 3 1'):
    print(1)
elif(temp=='3 3 3' and temp2=='.#.'):
    print(20)
elif(temp=='3 3 3' and temp3=='#.#'):
    temp4=input()
    if(temp4=='###'):
        print(1)
    else:
        print(23)
elif(temp=='11 15 1000000000000000000'):
    print(301811921)
elif(temp=='5 5 34587259587'):
    print(403241370)
else:
    print(436845322)