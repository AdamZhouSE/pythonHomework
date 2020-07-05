def judge(string):
    string = list(string)
    string.sort()
    result = ""
    pre = string[0]
    situation = True
    for temp in range(1,len((string))):
        if(string[temp]==pre):
            situation = False
        else:
            if(situation):
                if(ord(pre)>=ord('a') and ord(pre)<=ord('z')):
                    result += pre;
                pre = string[temp]
            else:
                pre = string[temp]
                situation = True
    if(situation):
        result += string[-1]
    if(len(result) %2 == 1):
        print("HE!")
    else:
        print("SHE!")

n = eval(input())
while( n > 0):
    n = n - 1
    judge(input())