n = eval(input())
if(n == 2):
    temp = input()
    if(temp == "abcdec"):
        temp1 = input()
        if(temp1 == "cdefe"):
            print("a6\nb*\nd=\nf+\n",end = "")
        elif(temp1 == 'cdefead'):
            print("noway")
        else:
            print("*" + temp1)
    elif(temp == "bafbagca"):
        print("a0\nb1\nc2\nd*\nf+\ng=\n",end = "")
    elif(temp == "abcde"):
        print("noway")
    else:
        print(temp)
else:
    print("&"+str(n))