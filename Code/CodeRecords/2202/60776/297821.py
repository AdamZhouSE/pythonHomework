def digui(a):
    if a==1 or a==2:
        return a
    else:
        return digui(a-1)+digui(a-2)

if __name__ == "__main__":
    a=int(input())
    for i in range(0,a):
        a=int(input())
        print(digui(a))