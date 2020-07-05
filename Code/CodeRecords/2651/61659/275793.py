T=int(input())

for i in range(0,T):
    num=int(input())
    binary=bin(num)
    binary=binary[2:]
    while len(binary)<8:
        binary="0"+binary

    for i in range(0,4):
        x=binary[2*i]
        y=binary[2*i+1]
        binary=binary[:2*i]+y+x+binary[2*i+2:]

    print(int(binary,2))
