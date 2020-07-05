class Ykf:
    def __init__(self,alpha,order):
        self.order=order
        self.alpha=alpha

alphabet=list(input())
answer=[]
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
        print(i.order,end=" ")
        answer.remove(i)
print()