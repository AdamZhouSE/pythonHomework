import math
T = eval(input())
Test_num = []
Test_t = []
medium_1 = 0
medium_2 = 0
medium = 0
t = []
for i in range(T):
    Test_num.append(eval(input()))
    Test_t.append(input())
for i in range(T):
    Test_t[i].split()
    if Test_num[i]%2 == 0:
        
#        print(int(math.floor((Test_t[i][int(int(Test_num[i])/2)]+Test_t[i][int(int(Test_num[i])/2-1)])/2)))