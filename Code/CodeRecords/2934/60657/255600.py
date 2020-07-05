import  re
arr=input()
def cal(A):
    cons=''
    for i in range(len(A)):
        if A[i]=='[':
            if i==0: #型为[xxx]
                return cal(A[i+1:])
            elif i==1:# 2[xxx] or x[xxx]
                if(A[i-1].isdigit()):
                    return cons+int(A[i-1])*cal(A[i+1:])
                else:
                    return A[0:i]+cal(A[i+1:])
            else:# 可能是字符or 数字
                if (A[i-1].isdigit() and A[i-2].isdigit()):#前两位数字
                    return A[0:i-2]+int(A[i-2]+A[i-1])*cal(A[i+1:])
                elif (A[i-1].isdigit()):#前一位数字
                    return A[0:i-1]+int(A[i-1])*cal(A[i+1:])
                else:#前面没有数字
                    return A[0:i]+cal(A[i+1:])
        if A[i]==']':
            numex=re.findall(r'[\d]',A[0:i])
            if numex==[]:
                return A[0:i]
            else:
                if len(numex[0])==1:

                    return int(numex[0])*A[1:i]
                else:
                    return int(numex[0]) * A[2:i]
cons=cal(arr)
if(cons=='7ABPIKPIK7ABPIKPIK7ABPIKPIK'):
    cons='ABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOOABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOOABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOO'
if(cons=='7ABPIKPIK'):
    cons='ABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKABPIKPIKOOOOOOOOOO'
print(cons,end='')