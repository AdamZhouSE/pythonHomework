def exam5():
    i=input().split(" ")
    i.remove("0")
    string=i[0]
    for j in range(len(i)-1,0):
        string=string+" "+i[j]
    print(string,end=" ")
exam5()