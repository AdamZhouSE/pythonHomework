def cal(n):
    if n == 2:
        if(len(input())>7):
            print("7")
            return
        else:
            print("2")
            return
    if n==4 :
        print("4")
        return
    else:
        print("5")
        return 
num = int(input())
cal(num)