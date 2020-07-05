num = int(input())
for i in range(num):
    Str=input()
    if len(Str)%2!=0:
        print('not balanced')
    else:
        for index in range(len(Str)//2):
            if Str[index]=='[':
                if Str[len(Str)-index-1]!=']':
                    print('not balanced')
                    break
            elif Str[index]=='{':
                if Str[len(Str)-index-1]!='}':
                    print('not balanced')
                    break
            elif Str[index]=='(':
                if Str[len(Str)-index-1]!=')':
                    print('not balanced')
                    break
        print('balanced')