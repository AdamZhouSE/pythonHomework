def restDay(infor):
    if(len(infor)==1):
        if(infor[0]==0):
            return 1
        else:
            return 0
    else:
        if(infor[0]==0):
            return 1+restDay(infor[1:])
        elif(infor[0]==1):
            if(infor[1]==0 or infor[1]==2):
                return restDay(infor[1:])
            elif(infor[1]==1):
                return min(1+restDay(infor[1:]),restDay([0]+infor[2:]))
            else:
                return min(1+restDay(infor[1:]),restDay([2]+infor[2:]))
        elif(infor[0]==2):
            if(infor[1]==0 or infor[1]==1):
                return restDay(infor[1:])
            elif(infor[1]==2):
                return min(1+restDay(infor[1:]),restDay([0]+infor[2:]))
            else:
                return min(1+restDay(infor[1:]),restDay([1]+infor[2:]))
        elif(infor[0]==3):
            return restDay(infor[1:])
n=int(input())
infor=list(map(int,input().split(" ")))
print(restDay(infor)) 