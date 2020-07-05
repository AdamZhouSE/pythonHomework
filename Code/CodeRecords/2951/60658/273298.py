def get(arr,base):
    res = 0
    temp = 1
    for i in arr[::-1]:
        res+=int(i)*temp
        temp*=base
    return res

binary = list(input())
thri = list(input())
ans = 0
for i in range(len(binary)):
    binary[i]="1" if binary[i]=="0" else "0"
    for j in range(len(thri)):
        raw = thri[j]
        for k in range(3):
            if str(k)==raw:
                continue
            thri[j]=str(k)
            if get(thri,3)==get(binary,2):
                print(get(binary,2),end="")
                exit()              
        thri[j]=raw
    binary[i]="1" if binary[i]=="0" else "0"