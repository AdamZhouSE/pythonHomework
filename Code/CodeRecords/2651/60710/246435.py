#奇偶数的交换

def change(s):
    re=s[1:2]+s[0:1]
    return re

def solve(num):
    the_bin=bin(num).replace('0b','') #这个数字对应的二进制字符串
    if len(the_bin)%2==0:
        the_bin="00"+the_bin
    else:
        the_bin="000"+the_bin
    #print(the_bin)
    re=""
    i=0
    while i<len(the_bin)-1:
        t=the_bin[i:i+2]
        #print(t)
        re=re+change(t)
        i=i+2
        #print(re)
    re='0b'+re
    return int(re,2)

if __name__ == '__main__':
    a=int(input())
    c=0
    while c<a:
        num=int(input())
        print(solve(num))
        c=c+1
