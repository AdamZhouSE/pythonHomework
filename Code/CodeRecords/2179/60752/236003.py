line1=input().split(' ')
str_len=int(line1[0])
str_num=int(line1[1])
string=input()
for i in range(0,str_num):
    line=list(map(int,input().split(' ')))
    s1=string[line[0]:line[1]+1]
    s2=string[line[2]:line[3]+1]
    counter=0
    while True:
        if s1[counter]==s2[counter]:
            counter=counter+1
            if counter==len(s1) or counter==len(s2):
                print(counter)
                break
        else:
            print(counter)
            break