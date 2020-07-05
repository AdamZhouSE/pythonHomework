inp = input()
list = inp[1:len(inp)-1].split(",")
i=0
while(i<len(list)):
    if(list[i]==list[i+1]):
        i+=2
    else:
        print(list[i])
        break


        