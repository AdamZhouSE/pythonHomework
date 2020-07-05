def ispre(a,b):
    if(len(a)>len(b)):
        a,b=b,a
    for i in range(0,len(b)+1):
        if a==b[0:i]:
            return True
    return False

index=1


while True:
    get=[]
    n=''
    b=False
    while True:
        n=input()
        if n=='9':
            break
        get.append(n)
    for i in range(0,len(get)):
        if b:
            break
        for j in range(i+1,len(get)):
            if ispre(get[i],get[j]):
                print('Set '+ str(index)+ ' is not immediately decodable')
                b=True
                break
            if i==len(get)-2 and j==len(get)-1:
                print('Set '+str(index)+' is immediately decodable')
    index+=1