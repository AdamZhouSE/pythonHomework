num = int(input())
factor = 1
cox = 1
bound = 0
while bound <= num:
    bound += cox * factor * 9
    cox += 1
    factor *= 10
cox -= 1
factor //= 10
bound -= cox * factor * 9
the_num = 10 ** (cox-1)
the_num += (num-bound-1) // cox
num = (num-bound) % cox
if num == 0:
    num = cox
print(str(the_num)[num-1])
