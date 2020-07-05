"""文字处理软件"""
def func4():
    n = int(input())
    op_str = input()
    while n>0:
        temp = input()
        if temp[0] == "1":
            op_str += temp[2:]
            print(op_str)
        elif temp[0] == "2":
            li = list(map(int, temp.split(" ")))
            op_str = op_str[li[1]:li[2]+li[1]]
            print(op_str)
        elif temp[0] == "3":
            li = temp.split(" ")
            op_str = op_str[0:int(li[1])] + li[2] +op_str[int(li[1]):]
            print(op_str)
        else:
            print(op_str.find(temp[2:]))

    return

func4()