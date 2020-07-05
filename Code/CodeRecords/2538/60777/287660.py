temp=input()
temp=temp[1:len(temp)-1]
temp=[int(x) for x in temp.split(',')]
i=1
while(True):
    if i not in temp:
        print(i)
        break
    i+=1