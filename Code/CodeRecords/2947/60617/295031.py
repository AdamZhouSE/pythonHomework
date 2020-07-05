def words_operator():
    N=int(input())
    str=input()
    for i in range(0,N):
        row=input().split(" ")
        operation=int(row[0])
        if operation==1:
            str+=row[1]
            print(str)
        elif operation==2:
            start=int(row[1])
            length=int(row[2])
            str=str[start:start+length]
            print(str)
        elif operation==3:
            insert_loc=int(row[1])
            insert_str=row[2]
            str=str[0:insert_loc]+insert_str+str[insert_loc:]
            print(str)
        elif operation==4:
            target_str=row[1]
            print(str.find(target_str, 0, len(str)))

if __name__=='__main__':
    words_operator()