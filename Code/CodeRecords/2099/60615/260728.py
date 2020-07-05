def convert(seq):
    table = {}
    for i in range(ord('A'), ord('Z') + 1):
        table[chr(i)] =i - ord('A')+1
    seq=[i for i in seq]
    seq.reverse()
    output=0
    for i in range(0,len(seq)):
        output=output+table[seq[i]]*26**i

    return  output
seq=input()
print(convert(seq))