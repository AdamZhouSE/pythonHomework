"""
您将获得一个具有6个面的立方体骰子
所有单独的面孔都印有一个数字,像任何普通骰子一样，数字在1到6的范围内
您将获得该立方体的一个面，您的任务是猜测立方体相反面上的数字
6-1,2-5,3-4
"""

n = int(input())
string_list = []

for i in range(n):
    string_list.append(int(input()))

for i in range(n):
    N = string_list[i]
    
    if N==6:
        print(1)
    elif N==1:
        print(6)
    elif N==2:
        print(5)
    elif N==5:
        print(2)
    elif N==3:
        print(4)
    elif N==4:
        print(3)
