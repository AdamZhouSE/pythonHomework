if __name__=='__main__':
    string = input()
    list_s = []
    string_s=""
    for i in range(len(string)):
        if(string[i]!='P'and string[i]!='B'):
            string_s = string_s + string[i]
        elif(string[i]=='P'):
            list_s.append(string_s)
        elif(string[i]=='B'):
            string_s = string_s[:-1]
    for i in range(int(input())):
        co = 0
        m,n = input().split()
        m = int(m)-1
        n = int(n)-1
        if list_s[m]>list_s[n]:
            co = 0
        else:
            co = list_s[n].count(list_s[m])
        print(co)


            