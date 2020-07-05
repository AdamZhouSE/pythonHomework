t = int(input())
for i in range(t):
    n = int(input())
    inp = [int(x) for x in input().split(" ")]
    inp.sort()
    max_subSeq = 1
    curr_subSeq = 1
    for j in range(n-1):
        if inp[j+1]-inp[j] == 1:
            curr_subSeq += 1
        else:
            max_subSeq = max(max_subSeq, curr_subSeq)
            curr_subSeq = 1
    print(max_subSeq)
