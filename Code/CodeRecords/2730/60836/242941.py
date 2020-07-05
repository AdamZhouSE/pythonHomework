"""
给定一个整数数组，任务是查找是否有可能使用这些数字的所有数字来构造一个整数
使得该整数可以被3整除
如果可能，则打印“ 1”，否则打印“ 0” 。
"""


n=int(input())
string_list = []

for i in range(n*2):
    string_list.append(str(input()))

i=0
while i<len(string_list):
    N=int(string_list[i])
    num_list=string_list[i+1].split()
    
    number=0
    for ch in num_list:
        number=number+int(ch)
        
    if number%3==0:
        print(1)
    else:
        print(0)
    i=i+2
