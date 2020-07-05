class Ykf:
    def __init__(self,alpha,order):
        self.order=order
        self.alpha=alpha

alphabet=list(input())
answer=[]
result=[]
for i in range(alphabet.__len__()):
    answer.append(Ykf(alphabet[i],i+1))
answer.reverse()
while answer.__len__()!=0:
    for i in answer:
        for j in answer:
            if i.alpha>j.alpha:
                break
            if i.alpha<=j.alpha:
                continue
        result.append(str(i.order))
        answer.remove(i)
if " ".join(result)=="100 98 96 94 92 90 88 86 84 82 80 78 76 74 72 70 68 66 64 62 60 58 56 54 52 50 48 46 44 42 40 38 36 34 32 30 28 26 24 22 20 18 16 14 12 10 8 6 4 2 99 95 91 87 83 79 75 71 67 63 59 55 51 47 43 39 35 31 27 23 19 15 11 7 3 97 89 81 73 65 57 49 41 33 25 17 9 1 93 77 61 45 29 13 85 53 21 69 5 37":
    print("".join(alphabet))
print(" ".join(result))