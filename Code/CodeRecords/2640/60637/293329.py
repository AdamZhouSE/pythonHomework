string=input()
target=input()
def detect(substr,target):
    for i in target:
        if(i not in substr):
            return False
    return True
record_length=float('Inf')
record_str=''
n=len(string)
for i in range(n):
    if(string[i] in target):
        j=i+1
        length=1
        while(j<=n and not detect(string[i:j],target)):
            j+=1
            length+=1
        if(detect(string[i:j],target) and length<record_length):
            record_length=length
            record_str=string[i:j]
print(record_str)