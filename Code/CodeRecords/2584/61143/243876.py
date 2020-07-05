num = eval(input())
#if num <= 3:
#   print("True")
#elif num == 4:
#   print("False")
#else:
#   print("True")
#两人一回合拿走的石子数量有：2、3、4、5、6
#所以4的倍数的石头会输
if num % 4 == 0:
    print("False")
else:
    print("True")