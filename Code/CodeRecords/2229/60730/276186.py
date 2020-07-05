# 一个局部倒置也是一个全局倒置，因此只需要检查有没有非局部倒置就可以了
tmp = list(map(int, input().split(",")))
length = len(tmp)
for i in range(length):
    for j in range(i+2,length):
        if tmp[i]>tmp[j]:
            print("False")
            exit()
print("True")
