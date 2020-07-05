min=10000000

def digui(list,index,bushu):
    global min
    if index==len(list)-1:
        if bushu<min:
            min=bushu
    else:
        for i in range(index+1,len(list)):
            if list[i]==list[index]:
                digui(list,i,bushu+1)
        digui(list,index+1,bushu+1)


if __name__ == "__main__":
    a=input().split(" = ")
    a=a[1]
    a=a.replace("{","")
    a=a.replace("}","")
    b=a.split(", ")
    for i in range(0,len(b)):
        b[i]=int(b[i])
    digui(b,0,0)
    print(min+1)