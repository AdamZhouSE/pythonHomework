def digui(list,a):
    list.append(a)
    if a>1:
        digui(list,a-1)


if __name__ == "__main__":
    a=int(input())
    for i in range(0,a):
        b=int(input())
        list=[]
        digui(list,b)
        list.reverse()
        print(" ".join(str(i) for i in list),end=" ")
        print()