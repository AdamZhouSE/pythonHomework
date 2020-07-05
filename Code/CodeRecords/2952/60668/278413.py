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
        for j in range(len(list_s[n])):
            if len(list_s[n])>len(list_s[m]):
                co = 0
            else:
                if list_s[n][j:j+len(list_s[m])+1]==list_s[m]:
                    co += 1
        print(co)

            