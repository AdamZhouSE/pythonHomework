def Print(string):
    nowprint=""
    printer=[]
    for i in range(len(string)):
        if string[i]=='B':
            nowprint=nowprint.replace(nowprint[len(nowprint)-1],'')
        elif string[i]=='P':
            printer.append(nowprint)
        else:
            nowprint+=string[i]
    return printer

def Func1(ask,printer):
    for i in range(len(ask)):
        string=printer[ask[i][0]]
        count=0
        for start in range(len(printer[ask[i][1]])-len(string)+1):
            if string==printer[ask[i][1]][start:start+len(string)]:
                count+=1
        print(count)

string=input()
m=int(input())
ask=[]
for i in range(m):
    ask.append(list(map(int,input().split(' '))))
printer=Print(string)
Func1(ask,printer)