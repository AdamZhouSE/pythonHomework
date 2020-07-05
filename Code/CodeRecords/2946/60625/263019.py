string=list(input())
count=0
check=0
for i in range(1,len(string)+1):
    if '0' not in string:
        print(count,end='')
        check=1
        break
    if i <len(string):
        if string[i] != string[i - 1]:
            count += 1
            for index in range(i):
                if string[index] == '1':
                    string[index] = '0'
                else:
                    string[index] = '1'
    else:
        if '1' not in string:
            count += 1
            for index in range(i):
                if string[index] == '1':
                    string[index] = '0'
                else:
                    string[index] = '1'

if check==0:
    print(count,end='')

