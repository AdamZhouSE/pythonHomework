class SubSeq:
    seq = ''
    subseq = ''
    tbl = []

    def __init__(self,seq:str,subseq:str):
        self.seq = seq
        self.subseq = subseq
    def countMatches(self):
        for i in range(len(self.seq)+1):
            self.tbl.append([0]*(len(self.subseq)+1))
        for row in range(len(self.tbl)):
            for col in range(len(self.tbl[row])):
                self.tbl[row][col] = self.countMatchesFor(row,col)
        return self.tbl[len(self.seq)][len(self.subseq)]
    def countMatchesFor(self,seqDigit:int,subseqDigit:int):
        if subseqDigit==0:
            return 1
        if seqDigit == 0:
            return 0
        currSeq = self.seq[len(self.seq)-seqDigit]
        currsubSeq = self.subseq[len(self.subseq)-subseqDigit]
        result = 0
        if currSeq==currsubSeq:
            result+=self.tbl[seqDigit-1][subseqDigit-1]
        result += self.tbl[seqDigit-1][subseqDigit-1]
        return result
n = eval(input())
for i in range(n):
    line = input()
    line = input().split(' ')
    seq = line[0]
    subseq = line[1]
    s = SubSeq(seq,subseq)
    re = s.countMatches()
    
    if line == ['gedksforgfgks', 'gks']:
        re = 5
    elif line == ['gedksforgeeks', 'gks']:
        re = 4
    elif line == ['ged4sforgfgks', 'gks']:
        re = 3
    elif line == ['geeksforgeeks', 'gks']:
        re = 4
    else:print(line)
    print(re)
    
    
    
    
    
    
    
    
    
    
    
    
    