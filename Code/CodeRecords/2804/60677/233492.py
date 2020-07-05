string=input()
if string.__len__()==1:
    print(string)
else:
    list=string.split('+')
    for i in range(0,len(list)-1):
        for j in range(i+1,len(list)):
            if int(list[i])>int(list[j]):
                t=list[i]
                list[i]=list[j]
                list[j]=t

    print('+'.join(list))