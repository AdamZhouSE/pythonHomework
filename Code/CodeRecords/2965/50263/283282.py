num1,num2 = input().split(' ')
string = input()
n = int(input())
for i in range(n):
    a,b,c = input().split(' ')
    d = int(a)
    e = int(b)
    f = int(c)
    string = string[0:f] + string[d:e]+string[f:len(string)]
    string = string[0:min(int(num2),len(string))]
print(string[0:int(num1)],end= '')