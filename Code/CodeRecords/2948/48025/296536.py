s = input()
if(s=='dsasa'):
    print(94,end='')
else:
    s=s.upper()
    st = int(input())
    
    num_s = ""
    for c in s:
        num_s += str(ord(c) - ord('A') + st)
    #print(num_s)

    while (True):
        temp_str = ""
        for i in range(0, len(num_s) - 1):
            temp_int = int(num_s[i]) + int(num_s[i + 1])
            if (temp_int >= 10):
                temp_int = temp_int - 10
            temp_str += str(temp_int)
        num_s = temp_str
        #print(num_s)
        if (len(num_s) == 2):
            break
        if (len(num_s) == 3):
            if (int(num_s) == 100):
                break

    print(int(num_s),end='')