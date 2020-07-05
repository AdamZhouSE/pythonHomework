isright=False

def digui(list,he,k,shu):
    global isright
    if not isright:
        if shu==1:
            for i in range(0,len(list)):
                if (he+list[i])%k==0:
                    isright=True
        else:
            for i in range(0,len(list)):
                list3=[]
                list3.extend(list)
                list3.remove(list[i])
                digui(list3,he+list[i],k,shu-1)





if __name__ == "__main__":
    b=input().split(',')
    for i in range(0,len(b)):
        b[i]=int(b[i])
    k=int(input())
    for i in range(2,len(b)+1):
        digui(b,0,k,i)
    print(isright)