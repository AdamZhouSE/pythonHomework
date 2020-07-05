def de(list,i):
    if i == len(list):
        list.remove(list[0])
    else:
        list.remove(list[i])


if __name__ == "__main__":
    a = int(input())
    for k in range(0,a):
        a=int(input())
        b=[]
        for i in range(1,a+1):
           b.append(i)
        i=0
        while len(b)!=1:
            if i>=len(b):
                i=0
            de(b,i+1)
            i=i+1
        print(b[0])