n = int(input())
x = 0
while x < n:
    x+=1
    a = input()
    b = input()
    
    if(len(a) > len(b) or (len(a) == len(b) and a != b)):
        print('No')
    elif(len(a)==len(b) and a==b):
        print('Yes')
    else:
        result = True
        index = 0
        a0 = a[0]
        for i in range(len(a)):
            if(i==len(a)-1 and a[i] == a[0] and b[i+1] == a[0]):
                result = False
                break
            if(a[0] == a[i] and b[i] != a[i]):
                result = False
                break
            if(a[0]!=a[i] and b[i] == b[i-1]):
                result = False
                break
            elif(a[0] != a[i] and b[i] != b[i-1]):
                break
                
        if result:
            index = 0
            for i in range(len(a)):
                while a[i] != b[i+index]:
                    index += 1
                    if index > len(b) - len(a):
                        print(len(a),len(b))
                        result = False
                        break
        
        if(result):
            print('Yes')
        else:
            print('No')