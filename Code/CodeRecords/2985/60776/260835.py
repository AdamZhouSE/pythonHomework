def digui(a,b):
    if a==1:
         print(chr(b),end="")
    else:
        digui(a-1,b-1)
        print(chr(b),end="")
        digui(a - 1, b - 1)
if __name__ == "__main__":
    a = int(input())
    c=65+a-1
    digui(a,c)
    print()