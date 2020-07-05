def find(string,pattern):
    for temp in string:
        if(temp in pattern):
            return temp
    return "$"

n = eval(input())
while(n!=0):
    n = n - 1
    string = input()
    patt = input()
    print(find(string,patt))