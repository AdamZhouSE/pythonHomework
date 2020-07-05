def count(matching):
    result=0
    for length in range(1,len(matching)+1):
        hasUsed=[]
        for start in range(len(matching)-length+1):
            thisMatch=matching[start:start+length]
            exist=0
            for i in range(len(hasUsed)):
                if thisMatch==hasUsed[i]:
                    exist=1
                    break
            if exist==0:
                result+=1
                hasUsed.append(thisMatch)
    return result

n=int(input())
string="".join(list(map(str,input().split(' '))))
for i in range(len(string)):
    print(count(string[0:i+1]))